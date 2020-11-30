<template>
  <div class="search container">
    <h2>Search by Movie Title!</h2>
    <b-row>
      <b-col><b-form-input v-model="actorName" placeholder="Enter Movie Title"></b-form-input></b-col>
      <b-col lg="2"><b-button @click="search" pill variant="outline-success">search <b-icon icon="search"></b-icon></b-button></b-col>
    </b-row>
    <b-spinner v-if="spinner" variant="primary" type="grow" label="Spinning"></b-spinner>
    <SearchResultCom v-if="show" :searchResult='searchResult'/>
    <h1 v-if="no_result">No Result</h1>
  </div>
</template>

<script>
import SearchResultCom from './SearchResult.vue'
const axios = require('axios'),
      util  = require('util');

export default {
  components: { SearchResultCom },
  name: 'search',
  props: {
    msg: String
  },
  data() {
    return {
      actorName: "",
      show: false,
      no_result: false,
      spinner: false,
      searchResult: {}
    }
  },
  methods: {
    search: function(){
      this.spinner = true
      var type = "Movie_Title"
      //send request to backend/database for search result
      var url = util.format("http://localhost:8081/%s?input=%s", type, this.actorName)
      axios
        .get(url)
        .then((response) =>{
          this.spinner = false
          this.searchResult = response.data
          if(this.searchResult.found != 0){
              this.show = true
          } else {
              this.no_result = true
          }
          console.log(response.data)
        })
        .catch(err => console.log(err))
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
