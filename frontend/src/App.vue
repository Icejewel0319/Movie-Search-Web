<template>
  <div id="app" >
    <!-- <img alt="logo" src="./assets/video-camera.png"> -->
    <Title/>

    

    <!-- <b-row class="bnts">
      <b-col></b-col>
      <b-col>Choose what you want to search: </b-col>
      <b-col ><b-button @click="tabChange" data-id="1" variant="outline-secondary">Actor</b-button></b-col>
      <b-col ><b-button @click="tabChange" data-id="2" variant="outline-secondary">Movie</b-button></b-col>
      <b-col ><b-button @click="tabChange" data-id="3" variant="outline-secondary">Released Year</b-button></b-col>
      <b-col></b-col>
      <b-col></b-col>
    </b-row> -->
    
    <!-- router -->
    <router-view></router-view>

    <!-- <SearchCom v-if="tab==1" msg="Actor's Name"/>
    <SearchCom v-else-if="tab==2" msg="Movie Title"/>
    <SearchCom v-else msg="Released Year"/> -->
  </div>
</template>

<script>
import Title from './components/Title.vue'
// import SearchCom from './components/Search.vue'

export default {
  name: 'App',
  components: { 
    Title, 
    // SearchCom, 
  },
  data() {
    return {
      tab: 1
    }
  },
  methods: {
    tabChange: function(e){
      // console.log(e.target.dataset)
      this.tab = e.target.dataset.id
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* margin-top: 60px; */
}

.bnts {
  margin-top: 20px;
}
</style>
