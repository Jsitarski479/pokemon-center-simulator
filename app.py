from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv  
import os                      

load_dotenv()  


app = Flask(__name__)

CORS(app)


# Set up the database URI (use your correct database)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def make_aware(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt

# Define the Pokeball model
class Pokeball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))
    pokemon_name = db.Column(db.String(100))
    trainer_name = db.Column(db.String(100))
    message = db.Column(db.String(255))
    expiration_time = db.Column(db.DateTime(timezone=True))
    trainer_image = db.Column(db.String(255))

# Route to get all pokeballs
@app.route('/pokeballs', methods=['GET'])
def get_pokeballs():
    pokeballs = Pokeball.query.all()
    now = datetime.now(timezone.utc)

    for pokeball in pokeballs:

        #if pokeball.expiration_time and pokeball.expiration_time.tzinfo is None:
            #print(f"Before: {pokeball.expiration_time}, tzinfo={pokeball.expiration_time.tzinfo}")
            #pokeball.expiration_time = pokeball.expiration_time.replace(tzinfo=timezone.utc)
            #print(f"After: {pokeball.expiration_time}, tzinfo={pokeball.expiration_time.tzinfo}")
        if (
            pokeball.status == 'closed' and 
            pokeball.expiration_time and 
            make_aware(pokeball.expiration_time) < now
        ):
            pokeball.status = 'open'
            pokeball.pokemon_name = None
            pokeball.trainer_name = None
            pokeball.message = None
            pokeball.trainer_image = None
            pokeball.expiration_time = None

    db.session.commit()

    return jsonify([{
        'id': pokeball.id,
        'status': pokeball.status,
        'pokemon_name': pokeball.pokemon_name,
        'trainer_name': pokeball.trainer_name,
        'message': pokeball.message,
        'expiration_time': pokeball.expiration_time.isoformat() if pokeball.expiration_time else None,
        'trainer_image': pokeball.trainer_image
    } for pokeball in pokeballs])

# Route to create a new pokeball entry (this is where the user submits data)
@app.route('/pokeballs', methods=['POST'])
def create_pokeball():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Create a new Pokeball entry using the provided data
        new_pokeball = Pokeball(
            status=data.get('status'),
            pokemon_name=data.get('pokemon_name'),
            trainer_name=data.get('trainer_name'),
            message=data.get('message'),
            expiration_time=datetime.strptime(data.get('expiration_time'), '%Y-%m-%d %H:%M:%S'),
            trainer_image=data.get('trainer_image')
        )
        
        # Add and commit the new pokeball to the database
        db.session.add(new_pokeball)
        db.session.commit()
        
        return jsonify({'message': 'Pokeball created successfully'}), 201
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during the request'}), 500

# Route to update the status of a pokeball (e.g., when it is used)
@app.route('/pokeball/<int:id>', methods=['PUT'])
def update_pokeball(id):
    try:
        data = request.get_json()
        print(f"Received data for Pokeball {id}: {data}")  # Debugging line
        
        if 'status' not in data or 'pokemon_name' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        pokeball = Pokeball.query.get(id)
        if pokeball:
            pokeball.status = data['status']
            pokeball.pokemon_name = data['pokemon_name']  # Store the selected Pokémon ID here
            pokeball.trainer_name = data['trainer_name']
            pokeball.message = data['message']
            pokeball.trainer_image = data['trainer_image']
            pokeball.expiration_time = datetime.now(timezone.utc) + timedelta(hours=24)
            db.session.commit()
            return jsonify({'message': 'Pokeball updated successfully'})
        else:
            return jsonify({'message': 'Pokeball not found'}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during the request'}), 500


# Run the Flask app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
