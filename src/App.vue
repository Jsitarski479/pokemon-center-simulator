<template>
  <v-app>
    <AudioPlayer ref="audioPlayer" />
    <v-container fluid>
      <router-view class="custom-router-view"></router-view>
      <v-row no-gutters>
        <v-col cols="8">
          <v-row no-gutters>
            <v-col cols="12">
              <div class="top-section">
                <h2 class="top_title">Pokémon Center Simulator</h2>
                <p class="testing">Welcome to the Pokémon Center Simulator! Here, you can select your 
                  favorite pokémon to rest at the center along with a message. You can only rest your pokémon if one of the
                  six spots are open. Feel free to select any of the closed pokéballs to see what other people have left.
                  (P.S. I'm hosting this on a free server, so please click anywhere on the screen to enable audio and give the site 
                  time; stuff takes a while to load)
                </p>
              </div>
            </v-col>

            <v-col cols="12">
              <div class="bottom-section">
                <v-img 
                  v-if="selectedPokeballData" 
                  class="pokemon-gif" 
                  :src="getPokemonImage(selectedPokeballData.pokemon_name)" 
                />
                <v-img 
                  v-if="selectedPokeballData" 
                  class="trainer" 
                  :src="getTrainerImage(selectedPokeballData.trainer_image)" 
                />
                <div class="info-container">
                  <div class = "pokemon_name_background">
                  <p class="pokemon-name" v-if="selectedPokeballData">
                  {{ getPokemonName(selectedPokeballData.pokemon_name) }}
                  </p>
                  </div>
                  <p class="user-name" v-if="selectedPokeballData">
                    {{ selectedPokeballData.trainer_name }}
                  </p>
                  <p class="time-check" v-if="selectedPokeballData">
                    {{ timeLeft(selectedPokeballData.expiration_time) }}
                  </p>
                  <p class="message" v-if="selectedPokeballData">
                    {{ selectedPokeballData.message }}
                  </p>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="4">
          <div class="right-section">
            <v-row class="pokeball-row">
              <v-col no-gutters cols="6" v-for="pokeball in pokeballs" :key="pokeball.id" class="my-0">
                <v-img
                class="pokeballs"
                :src="pokeball.status === 'closed' 
                ? require('@/assets/closed_pokeball.png') 
                : require('@/assets/open_pokeball.png')"
                @click="handlePokeballClick(pokeball)"
                />
                </v-col>
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import audioManager from '@/audioManager';
import pokemonNames from '@/pokemonNames';

export default {
  name: 'App',

  data() {
    return {
      selectedPokeballData: null
    };
  },

  mounted() {
    this.$store.dispatch('fetchPokeballs');

    // Defer audio playback until user clicks anywhere
    document.addEventListener('click', () => {
      audioManager.stop(); // Ensure clean playback
      audioManager.play().catch((e) => {
        console.warn('Autoplay failed:', e);
      });
    }, { once: true }); // Only register once
  },

  computed: {
    pokeballs() {
      return this.$store.getters.allPokeballs.slice().sort((a, b) => a.id - b.id);
    }
  },

  watch: {
    pokeballs(newVal) {
      const submittedTrainer = localStorage.getItem('submittedTrainer');
      const trainerStillPresent = newVal.some(
        (p) => p.trainer_name === submittedTrainer && p.status === 'closed'
      );
      if (!trainerStillPresent) {
        localStorage.removeItem('submittedTrainer');
      }
    }
  },

  methods: {
    timeLeft(expirationTime) {
      if (!expirationTime) return '';

      const expiration = new Date(expirationTime);
      const now = new Date();

      const nowUTC = Date.UTC(
        now.getUTCFullYear(),
        now.getUTCMonth(),
        now.getUTCDate(),
        now.getUTCHours(),
        now.getUTCMinutes(),
        now.getUTCSeconds()
      );

      const expirationUTC = Date.UTC(
        expiration.getUTCFullYear(),
        expiration.getUTCMonth(),
        expiration.getUTCDate(),
        expiration.getUTCHours(),
        expiration.getUTCMinutes(),
        expiration.getUTCSeconds()
      );

      const diff = expirationUTC - nowUTC;
      if (diff <= 0) return 'Expired';

      const hours = Math.floor(diff / (1000 * 60 * 60));
      const minutes = Math.floor((diff / (1000 * 60)) % 60);
      return `${hours}h ${minutes}m remaining`;
    },

    getPokemonName(id) {
      return pokemonNames[Number(id)] || 'Unknown';
    },

    handlePokeballClick(pokeball) {
      const submittedTrainer = localStorage.getItem('submittedTrainer');

      if (pokeball.status === 'closed') {
        this.selectedPokeballData = pokeball;
      } else {
        if (submittedTrainer) {
          alert('You already have a Pokémon in the center!');
          return;
        }
        this.selectedPokeballData = null;
        this.$router.push({ name: 'pokemon-form', query: { pokeball: pokeball.id } });
      }
    },

    getPokemonImage(id) {
      if (!id) return null;
      return require(`@/assets/pokemon_gifs/${id}.gif`);
    },

    getTrainerImage(id) {
      if (!id) return null;
      return require(`@/assets/trainers/${id}.png`);
    },

    formatDate(datetime) {
      if (!datetime) return '';
      const date = new Date(datetime);
      return date.toLocaleString();
    }
  }
};
</script>



<style scoped>
.v-application {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #555;
  border: 10px solid transparent;
  background-image: radial-gradient(circle, #ccc 20%, transparent 20%),
                    radial-gradient(circle, #333 20%, transparent 20%);
  background-size: 2vw 2vh;
  background-position: 0 0, 10px 10px;
}

.top-section {
  background-image: url("@/assets/pokemon_center_background_one.jpg");
  background-size: cover;
  background-position: center;
  padding: 10px;
  height: 40vh;
  border-bottom: 2px solid #000000;
}

.bottom-section {
  background-image: url("@/assets/testing_bottom_left_background.jpg");
  background-size: 60% 72%;
  background-position: 0 0;
  padding: 2vw;
  height: 84vh;
  width: 113vw;
}

.pokemon_name_background {
  position: relative;
  background-color: red;
  padding: 0.6vh 1.2vw;
  min-width: 12vw;
  border-radius: 8px;
}

.right-section {
  background-image: url("@/assets/pokemon_center_machine.jpg");
  background-size: cover;
  background-position: center;
  padding: 20px;
  height: 100vh;
  border-left: 2px solid #000000;
}

.top_title {
  font-family: 'Pokemon';
  font-size: 2.5vw;
}

.testing {
  font-family: 'Pokemon';
  font-size: 1vw;
}

.pokeballs {
  margin: 0;
  max-width: 6vw;
  max-height: 13vh;
  object-fit: contain;
}

.pokeball-row {
  margin-left: 3.7vw;
  margin-top: 25vh;
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}

.info-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1.2vh;
  margin-top: 2vh;
  margin-left: 2vw;
  max-width: 50vw;
  position: relative;
  z-index: 10;
}

.pokemon-name {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Pokemon';
  font-size: 1.8vw;
  color: white;
  pointer-events: none;
}

.user-name,
.time-check,
.message {
  font-family: 'Pokemon';
  font-size: 1vw;
  color: white;
}

.user-name {
  font-family: "Pokemon";
  font-size: 0.85vw;
}

.time-check {
  font-family: "Pokemon";
  font-size: 0.85vw;
}

.message {
  white-space: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
  max-width: 58vw;
  font-family: "Pokemon";
  font-size: 1.2vw;
}

.pokemon-gif {
  width:16.5vw;
  height:16.6vw;
}

.trainer {
  margin-top: -17vh;
  margin-left: 32vw;
  width:6.2vw;
  height: 8.6vw;
}

.custom-router-view {
  margin-left: -1.7vw;
  margin-top: -3.8vh;
}




</style>
