import Vue from 'vue';
import Router from 'vue-router';
import App from '@/App.vue'; // Home Page Component
import PokemonForm from '@/PokemonForm.vue'; // Form Page Component

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home', // Make sure this matches the name in goBack()
      component: App,
    },
    {
      path: '/pokemon-form',
      name: 'pokemon-form',
      component: PokemonForm,
    }
  ]
});
