<template>
  <div id="home">

      <h1>{{welcomeMsg}}</h1>
      <b-img up alt="Naslovan slika" :src="image"></b-img>


     <div class="navigation" >
      <ul>
          <router-link to="Igrac" ><b-button variant="outline-dark" style="margin-bottom: 5%; margin-right: 2%" >DODAJ IGRAČA</b-button></router-link>
          <router-link to="Tim"><b-button variant="outline-dark" style="margin-bottom: 5%; margin-right: 2%" >DODAJ TIM</b-button></router-link>

          <router-link to="Rezultati"><b-button variant="outline-dark" style="margin-bottom: 5%; margin-right: 2%">UNOS REZULTATA</b-button></router-link>
          <router-link to="Liga"><b-button variant="outline-dark" style="margin-bottom: 5%; margin-right: 2%">LIGA</b-button></router-link>

      </ul>
    </div>
  </div>


</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  data () {
    return {
      welcomeMsg: 'DOBRODOŠLI NA STRANICU PRVE HRVATSKE KUGLAŠKE LIGE',
    }
  },
  components: {
  },

  computed: {
    image () {
      return require('../assets/logo.jpg');
    }
  }
}
</script>
