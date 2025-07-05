import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';  // Import the router configuration file
import AudioPlayer from './AudioPlayer.vue';  // Import the AudioPlayer component
import store from './store'; // Import the Vuex store
import axios from 'axios';

Vue.prototype.$axios = axios;





import './assets/styles.css';


Vue.config.productionTip = false

Vue.component('AudioPlayer', AudioPlayer);

new Vue({
  store,
  router,
  vuetify,
  AudioPlayer,
  render: h => h(App),
}).$mount('#app')
