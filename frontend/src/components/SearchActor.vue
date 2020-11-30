<template>
  <div class="search container">
    <h2>Search by Actor's Name!</h2>
    <b-row>
        <b-col><b-form-input v-model="actorName" placeholder="Enter Actor's Name"></b-form-input></b-col>
        <b-col lg="2"><b-button @click="search" pill variant="outline-success">search <b-icon icon="search"></b-icon></b-button></b-col>
    </b-row>
    <ActorResultCom :searchResult="searchResult"/>
    <h1 v-if="no_result">No Result</h1>
  </div>
</template>

<script>
import ActorResultCom from './ActorResult.vue'
const axios = require('axios'),
      util  = require('util');

export default {
  components: { 
    // YearResultCom, 
    ActorResultCom 
  },
  name: 'search',
  props: {
    msg: String
  },
  data() {
    return {
      actorName: "",
      no_result: false,
      searchResult: {
        
      }
    }
  },
  methods: {
    search: function(){
      var type = "Actor's_Name"
      //send request to backend/database for search result
      var url = util.format("http://localhost:8081/%s?input=%s", type, this.actorName)
      axios
        .get(url)
        .then((response) =>{
          this.searchResult = response.data
          if(this.searchResult.found != 0){
              this.show = true
          } else {
              this.no_result = true
          }
        })
        .catch(err => console.log(err))
    },
    hideResult: function(){
      this.movie_show = false;
      this.actor_show = false;
      this.year_show = false;
    },
    resultList: function(){
      console.log(this.searchResult)
      console.log("ddd")
      return this.searchResult.result
    }
  },
  // watch: {
  //   searchResult: function(newVal){
  //       this.searchResult = newVal
  //       console.log(this.searchResult.result)
  //   }
  // }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
