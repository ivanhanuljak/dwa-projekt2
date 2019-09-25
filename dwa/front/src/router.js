import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Igrac from './views/Igrac'
import Tim from './views/Tim'
import Liga from './views/Liga'
import Rezultati from "./views/Rezultati";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },

    {
      path: '/Igrac',
      name: 'Igrac',
      component: Igrac
    },
    {
      path: '/Tim',
      name: 'Tim',
      component: Tim
    },
    {
      path: '/Liga',
      name: 'Liga',
      component: Liga
    },
    {
      path: '/Rezultati',
      name: 'Rezultati',
      component: Rezultati
    },
    ]
})
