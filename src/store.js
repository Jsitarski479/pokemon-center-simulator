import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    pokeballs: [
      { id: 1, isUsed: false, pokemonName: null, trainerName: null, message: null },
      { id: 2, isUsed: false, pokemonName: null, trainerName: null, message: null },
      { id: 3, isUsed: false, pokemonName: null, trainerName: null, message: null },
      { id: 4, isUsed: false, pokemonName: null, trainerName: null, message: null },
      { id: 5, isUsed: false, pokemonName: null, trainerName: null, message: null },
      { id: 6, isUsed: false, pokemonName: null, trainerName: null, message: null }
    ],
    isAudioPlaying: false, // New state to track audio status
  },
  mutations: {
    setPokeballs(state, pokeballs) {
      state.pokeballs = pokeballs;
    },
    updatePokeball(state, { id, pokemonName, trainerName, message }) {
      const pokeball = state.pokeballs.find(b => b.id === id);
      if (pokeball) {
        pokeball.isUsed = true;
        pokeball.pokemonName = pokemonName;
        pokeball.trainerName = trainerName;
        pokeball.message = message;
      }
      // update pokeball at id with pokeball
    },
    setAudioPlaying(state, status) {
      state.isAudioPlaying = status;
    }
  },
  actions: {
    fetchPokeballs({ commit }) {
      axios.get('http://10.0.0.141:5000/pokeballs')
        .then(response => {
          commit('setPokeballs', response.data);
        })
        .catch(error => console.error("Error fetching Pokéballs:", error));
    },
    storePokemon({ commit }, { id, pokemonName, trainerName, message }) {
      commit('updatePokeball', { id, pokemonName, trainerName, message });
    },
    initializeAudio({ commit }) {
      const audio = document.getElementById('audio-player');
      if (!audio.paused) {
        return; // Audio is already playing, do nothing
      }
      audio.play();
      commit('setAudioPlaying', true);
    },
    stopAudio({ commit }) {
      const audio = document.getElementById('audio-player');
      if (!audio.paused) {
        audio.pause();
        commit('setAudioPlaying', false);
      }
    },
    
  },
  getters: {
    allPokeballs: state => state.pokeballs,
    isAudioPlaying: state => state.isAudioPlaying
  }
});
