<template>
  <div class="search">
    <h2>Search by {{ msg }}</h2>
    <b-row>
    <b-col><b-form-input v-model="actorName" :placeholder="'Enter ' + msg"></b-form-input></b-col>
    <b-col lg="2"><b-button @click="search" pill variant="outline-success">search <b-icon icon="search"></b-icon></b-button></b-col>
    </b-row>
    <b-button variant="outline-secondary" @click="hideResult" v-if="click">close search result <b-icon icon="x-circle"></b-icon></b-button>
    <SearchResult v-if="click"  :searchResult='searchResult'/>
  </div>
</template>

<script>
import SearchResult from './SearchResult.vue'
const axios = require('axios'),
      util  = require('util');

export default {
  components: { SearchResult },
  name: 'search',
  props: {
    msg: String
  },
  data() {
    return {
      actorName: "",
      click: false,
      searchResult: {
        
      }
    }
  },
  methods: {
    search: function(){
      //change val
      this.click = true
      this.searchResult.name = this.actorName
      //send request to backend/database for search result
      var url = util.format("http://localhost:8081/test?name=%s", this.actorName)
      axios
        .get(url)
        .then(response =>(
          this.searchResult = response.data
          // console.log(response.data)
        ))
        .catch(err => console.log(err))
    },
    hideResult: function(){
      this.click = false;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
