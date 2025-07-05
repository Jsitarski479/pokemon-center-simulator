<template>
  <v-app class="everything">
    <v-container fluid>
      <router-view class="custom-router-view"></router-view>
      <v-row no-gutters>
        <v-col cols="6" class="input_section">
          <v-row no-gutters>
            <div class="selection_materials">
              <!-- Clicking this will trigger the goBack method -->
              <v-img class="arrow" :src="require('@/assets/left_arrow.png')" @click="goBack" />
              <div class="username_section">
                <p class="username_title">Trainer Name:</p>
                <input
                  v-model="trainerName"  
                  type="text"
                  minlength="4"
                  maxlength="26"
                  placeholder="Trainer name here"
                  class="username_input"
                />
              </div>
              <div class="message_section">
                <p class="message_title">Message:</p>
                <input
                  v-model="message"  
                  type="text"
                  minlength="4"
                  maxlength="90"
                  placeholder="Message here"
                  class="message_input"
                />
              </div>
              <div class="selection_buttons">
                <div class="selection-horizontal">
                  <h2 class="choose_your">Choose Your:</h2>
                  <div class="selection-verdical">
                    <button class="pokemon_button" @click="toggleSelection('pokemon')">Pokémon</button>
                    <button class="trainer_button" @click="toggleSelection('trainer')">Trainer</button>
                  </div>
                </div>
              </div>
              <button class="submit" @click="submitPokeball">Submit</button> <!-- Trigger the 'submitPokeball' method -->
            </div>
          </v-row>
        </v-col>

        <!-- Right Column - 5 Separate Grids for Pokémon and Trainers -->
        <v-col cols="6" class="right_section">
          <div class="grid-container">
            <!-- Wrapper for Pokémon grid -->
            <div v-if="selectedCategory === 'pokemon'" class="grid-column">
              <div v-for="pokemon in getColumnItems(1, 'pokemon')" :key="'pokemon-' + pokemon.id" class="grid-item" @mouseenter="hoveredPokemonId = pokemon.id" @mouseleave="hoveredPokemonId = null">
                <img 
                  :src="pokemon.src" 
                  alt="Pokemon" 
                  class="pokemon-gif"
                  :class="{'selected-pokemon': selectedPokemonId === pokemon.id}" 
                  @click="selectPokemon(pokemon.id)" 
                />
                <p v-if="hoveredPokemonId === pokemon.id" class="pokemon-hover-name">
                  {{ getPokemonName(pokemon.id) }}
                </p>
              </div>
            </div>

            <!-- Wrapper for Trainer grid -->
            <div v-else class="grid-column">
              <div v-for="trainer in getColumnItems(1, 'trainer')" :key="'trainer-' + trainer.id" class="grid-item">
                <img 
                  :src="trainer.src" 
                  alt="Trainer" 
                  class="trainer-gif"
                  :class="{'selected-trainer': selectedTrainerId === trainer.id}" 
                  @click="selectTrainer(trainer.id)" 
                />
              </div>
            </div>

            <!-- Repeat for Columns 2-5 -->
            <div v-if="selectedCategory === 'pokemon'" class="grid-column">
              <div v-for="pokemon in getColumnItems(2, 'pokemon')" :key="'pokemon-' + pokemon.id" class="grid-item" @mouseenter="hoveredPokemonId = pokemon.id" @mouseleave="hoveredPokemonId = null">
                <img 
                  :src="pokemon.src" 
                  alt="Pokemon" 
                  class="pokemon-gif"
                  :class="{'selected-pokemon': selectedPokemonId === pokemon.id}" 
                  @click="selectPokemon(pokemon.id)" 
                />
                <p v-if="hoveredPokemonId === pokemon.id" class="pokemon-hover-name">
                  {{ getPokemonName(pokemon.id) }}
                </p>
              </div>
            </div>
            <div v-else class="grid-column">
              <div v-for="trainer in getColumnItems(2, 'trainer')" :key="'trainer-' + trainer.id" class="grid-item">
                <img 
                  :src="trainer.src" 
                  alt="Trainer" 
                  class="trainer-gif"
                  :class="{'selected-trainer': selectedTrainerId === trainer.id}" 
                  @click="selectTrainer(trainer.id)" 
                />
              </div>
            </div>

            <!-- Repeat for Columns 3, 4, and 5 -->
            <div v-if="selectedCategory === 'pokemon'" class="grid-column">
              <div v-for="pokemon in getColumnItems(3, 'pokemon')" :key="'pokemon-' + pokemon.id" class="grid-item" @mouseenter="hoveredPokemonId = pokemon.id" @mouseleave="hoveredPokemonId = null">
                <img 
                  :src="pokemon.src" 
                  alt="Pokemon" 
                  class="pokemon-gif"
                  :class="{'selected-pokemon': selectedPokemonId === pokemon.id}" 
                  @click="selectPokemon(pokemon.id)" 
                />
                <p v-if="hoveredPokemonId === pokemon.id" class="pokemon-hover-name">
                  {{ getPokemonName(pokemon.id) }}
                </p>
              </div>
            </div>
            <div v-else class="grid-column">
              <div v-for="trainer in getColumnItems(3, 'trainer')" :key="'trainer-' + trainer.id" class="grid-item">
                <img 
                  :src="trainer.src" 
                  alt="Trainer" 
                  class="trainer-gif"
                  :class="{'selected-trainer': selectedTrainerId === trainer.id}" 
                  @click="selectTrainer(trainer.id)" 
                />
              </div>
            </div>

            <!-- Repeat for Columns 4 and 5 -->
            <div v-if="selectedCategory === 'pokemon'" class="grid-column">
              <div v-for="pokemon in getColumnItems(4, 'pokemon')" :key="'pokemon-' + pokemon.id" class="grid-item" @mouseenter="hoveredPokemonId = pokemon.id" @mouseleave="hoveredPokemonId = null">
                <img 
                  :src="pokemon.src" 
                  alt="Pokemon" 
                  class="pokemon-gif"
                  :class="{'selected-pokemon': selectedPokemonId === pokemon.id}" 
                  @click="selectPokemon(pokemon.id)" 
                />
                <p v-if="hoveredPokemonId === pokemon.id" class="pokemon-hover-name">
                  {{ getPokemonName(pokemon.id) }}
                </p>
              </div>
            </div>
            <div v-else class="grid-column">
              <div v-for="trainer in getColumnItems(4, 'trainer')" :key="'trainer-' + trainer.id" class="grid-item">
                <img 
                  :src="trainer.src" 
                  alt="Trainer" 
                  class="trainer-gif"
                  :class="{'selected-trainer': selectedTrainerId === trainer.id}" 
                  @click="selectTrainer(trainer.id)" 
                />
              </div>
            </div>

            <div v-if="selectedCategory === 'pokemon'" class="grid-column">
              <div v-for="pokemon in getColumnItems(5, 'pokemon')" :key="'pokemon-' + pokemon.id" class="grid-item" @mouseenter="hoveredPokemonId = pokemon.id" @mouseleave="hoveredPokemonId = null">
                <img 
                  :src="pokemon.src" 
                  alt="Pokemon" 
                  class="pokemon-gif"
                  :class="{'selected-pokemon': selectedPokemonId === pokemon.id}" 
                  @click="selectPokemon(pokemon.id)" 
                />
                <p v-if="hoveredPokemonId === pokemon.id" class="pokemon-hover-name">
                  {{ getPokemonName(pokemon.id) }}
                </p>
              </div>
            </div>
            <div v-else class="grid-column">
              <div v-for="trainer in getColumnItems(5, 'trainer')" :key="'trainer-' + trainer.id" class="grid-item">
                <img 
                  :src="trainer.src" 
                  alt="Trainer" 
                  class="trainer-gif"
                  :class="{'selected-trainer': selectedTrainerId === trainer.id}" 
                  @click="selectTrainer(trainer.id)" 
                />
              </div>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import pokemonNames from '@/pokemonNames';


export default {
  name: 'PokemonForm',
  data() {
    return {
      selectedCategory: 'pokemon', // Default to 'pokemon'
      hoveredPokemonId: null,
      trainerName: '',  // Bind input for trainer's name
      message: '', // Bind input for message
      selectedPokeballId: this.$route.query.pokeball, // Retrieve the pokeball id from the query string
      selectedPokemonId: null, // Store selected Pokémon ID
      selectedTrainerId: null, // Store selected Trainer ID
      pokemonList: [], // List of Pokémon objects (to be generated dynamically)
      trainerList: [] // List of Trainer objects (to be generated dynamically)
    };
  },
  methods: {
    getPokemonName(id) {
      return "Pokémon name: " + pokemonNames[Number(id)] || 'Unknown';
    },
    goBack() {
      // Navigate back to the home page
      this.$router.push({ name: 'home' });

      // Then stop audio after navigation
      this.$nextTick(() => {
        this.$store.dispatch('stopAudio');
      });
    },

    toggleSelection(category) {
      // Toggle between Pokémon and Trainer category
      this.selectedCategory = category;

      // Populate the appropriate list based on category
      if (category === 'pokemon') {
        this.pokemonList = this.generatePokemonList();
      } else {
        this.trainerList = this.generateTrainerList();
      }
    },

    // Capture selected Pokémon ID when clicked
    selectPokemon(pokemonId) {
      this.selectedPokemonId = pokemonId;  // Store the selected Pokémon ID
    },

    // Capture selected Trainer ID when clicked
    selectTrainer(trainerId) {
      this.selectedTrainerId = trainerId;  // Store the selected Trainer ID
    },

    generatePokemonList() {
      const pokemonList = [];
      // Dynamically generate Pokémon list
      for (let i = 1; i <= 649; i++) {
        pokemonList.push({
          id: i,
          src: require(`@/assets/pokemon_gifs/${i}.gif`) // Dynamically require Pokémon GIFs
        });
      }
      return pokemonList;
    },

    generateTrainerList() {
      const trainerList = [];
      // Dynamically generate Trainer list
      for (let i = 1; i <= 98; i++) {
        trainerList.push({
          id: i,
          src: require(`@/assets/trainers/${i}.png`) // Dynamically require Trainer images
        });
      }
      return trainerList;
    },

    getColumnItems(column, type) {
      // Fetch items for each column (adjusted to display items in vertical columns)
      const list = type === 'pokemon' ? this.pokemonList : this.trainerList;
      return list.filter((_, index) => (index % 5 === column - 1));
    },

    // Submit the form after checking all fields
    async submitPokeball() {
      // Check if Trainer Name, Message, Pokémon, and Trainer are selected
      if (!this.trainerName || !this.message || !this.selectedPokemonId || !this.selectedTrainerId) {
        alert('Please fill in all fields: Trainer Name, Message, Pokémon, and Trainer.');
        return;
      }

      try {
        const response = await this.$axios.put(`https://pokemon-center-backend.onrender.com/pokeball/${this.selectedPokeballId}`, {
          status: "closed", // Set status, can be dynamic
          pokemon_name: this.selectedPokemonId,  // Send the selected Pokémon ID here
          trainer_name: this.trainerName,  // Trainer name input
          message: this.message,  // Message input
          expiration_time: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString().slice(0, 19).replace('T', ' '),
          trainer_image: this.selectedTrainerId  // Trainer image (or whatever image the user selects)
        });
        console.log('Response:', response.data);
        // After successful update, navigate back to the home page
        this.$router.push({ name: 'home' });
        this.$nextTick(() => {
        this.$store.dispatch('stopAudio');
      });
      } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
      }
    }
  },
  mounted() {
    // Initially populate the Pokémon list
    this.pokemonList = this.generatePokemonList();
  }
};
</script>


<style scoped>
.selected-pokemon {
  border: 3px solid black; /* black outline for selected Pokémon */
  border-radius: 5px;  /* Optional: Rounded corners */
}

.selected-trainer {
  border: 3px solid black; /* black outline for selected Trainer */
  border-radius: 5px;  /* Optional: Rounded corners */
}

.pokemon-gif,.trainer-gif {
  max-width: 80%;
  max-height: 80%;
  object-fit: contain;
  transition: transform 0.1s ease-in-out;
}

.pokemon-gif:hover {
  transform: scale(1.3);
}

.input_section {
  height: 100vh;
  width: 66.67vw;
  background-image: url("@/assets/pokemon_x_background_two.jpg");
  background-size: cover;
  display: flex;
  flex-direction: column;
  position: relative;
  justify-content: space-between;
}

.arrow {
  max-width: 3vw;
  max-height: 5vh;
  height: auto;
}

.username_input {
  font-size: 3vh;
  font-family: 'Pokemon';
  word-wrap: break-word;
  overflow-wrap: break-word;
}

.username_title {
  font-family: 'Pokemon';
  font-size:3vh;
}

.message_title {
  font-size:3vh;
  font-family: 'Pokemon';
}

.message_input {
  font-size:3vh;
  font-family: 'Pokemon';
}

.choose_your {
  font-size: 3.8vh;
  font-family: 'Pokemon';
}

.pokemon_button {
  height: 10vh;
  font-size:3.8vh;
  font-family: 'Pokemon';
  background-color: gray;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  border-left: 2px solid black;
  border-right: 2px solid black;
  border-radius: 10px;
  margin-right: 1vw;
  width: 35vw;
  transition: ease 0.5s ease-in-out;
}

.trainer_button {
  font-size: 3.8vh;
  height: 10vh;
  font-family: 'Pokemon';
  background-color: gray;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  border-left: 2px solid black;
  border-right: 2px solid black;
  margin-right: 1vw;
  border-radius: 10px;
  transition: ease 0.5s ease-in-out;
}

.submit {
  font-size:3.8vh;
  font-family: 'Pokemon';
  height: 10vh;
  font-family: 'Pokemon';
  background-color: gray;
  border-radius: 10px;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  border-left: 2px solid black;
  border-right: 2px solid black;
  transition: transform 0.5s ease-in-out;
}

.pokemon_button:hover,
.trainer_button:hover,
.submit:hover{
  background-color: rgb(183, 183, 180);
}

.selection_materials {
  display: flex;
  flex-direction: column;
  gap: 5vw;
}

.username_section,
.message_section {
  display: flex;
  flex-direction: row;
}

.selection-horizontal {
  display: flex;
  flex-direction: row;
}

.selection-verdical {
  display: flex;
  flex-direction: column;
  gap: 1vw;
  margin-top: -3vw;
}

.right_section {
  background-image: url("@/assets/pokemon_x_background.jpg");
  background-size: cover;
  padding: 10px;
  overflow-y: auto;
  height: 100vh;
  border-left: 5px solid #000;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);  /* 5 columns */
  /*grid-gap: 10px;*/
  /*padding: 10px;*/
  overflow-y: auto;
  height: 100%;
}

.grid-column {
  display: flex;
  flex-direction: column;
  border-right: 5px solid #000;
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 150px;
  border-bottom: 5px solid #000;
}

.pokemon-hover-name {
  margin-top: 2vw;
  margin-left: 25vw;
  position: absolute;
  top: 5px;
  left: 5px;
  font-family: 'Pokemon';
  font-size: 0.85vw;
  color: black;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 2px 6px;
  border-radius: 4px;
  pointer-events: none;
}

.pokemon-gif,
.trainer-gif {
  max-width: 80%;
  max-height: 80%;
  object-fit: contain;
  transition: transform 0.1s ease-in-out;
}

.pokemon-gif:hover,
.trainer-gif:hover{
  transform: scale(1.3);
}

.pokemon-button,
.trainer-button {
  height: 10vh;
  font-family: 'Pokemon';
  background-color: gray;
  border-radius: 20px;
  width: 35vw;
}

.selection-buttons {
  display: flex;
  flex-direction: column;
}

::-webkit-scrollbar {
  width: auto; /* Set the width of the scrollbar */
}

::-webkit-scrollbar-track {
  background:rgb(106, 106, 106);
}

::-webkit-scrollbar-thumb {
  background:rgb(0, 0, 0);
}

::-webkit-scrollbar-thumb:hover {
  background: #777; /* Hover effect for the thumb */
}
</style>
