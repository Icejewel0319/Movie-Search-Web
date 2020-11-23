<template>
  <div class="search">
    <!-- <h2>Search by {{ msg }}</h2> -->
    <b-row>
    <b-col><b-form-input v-model="actorName" :placeholder="'Enter ' + msg"></b-form-input></b-col>
    <b-col lg="2"><b-button @click="search" pill variant="outline-success">search <b-icon icon="search"></b-icon></b-button></b-col>
    </b-row>
    <b-button variant="outline-secondary" @click="hideResult" >close search result <b-icon icon="x-circle"></b-icon></b-button>
    <SearchResultCom v-if="movie_show"  :searchResult='searchResult'/>
    <YearResultCom v-if="year_show" :searchResult="searchResult"/>
    <ActorResultCom v-if="actor_show" :searchResult="searchResult"></ActorResultCom>
  </div>
</template>

<script>
import SearchResultCom from './SearchResult.vue'
import YearResultCom from './ReleasedYearResult.vue'
import ActorResultCom from './ActorResult.vue'
const axios = require('axios'),
      util  = require('util');

export default {
  components: { SearchResultCom, YearResultCom, ActorResultCom },
  name: 'search',
  props: {
    msg: String
  },
  data() {
    return {
      actorName: "",
      movie_show: false,
      actor_show: false,
      year_show: false,
      searchResult: {
        
      }
    }
  },
  methods: {
    search: function(){
      var type = this._props.msg.split(" ").join("_")
      console.log(type)
      //change val
      if(type == "Movie_Title") this.movie_show = true
      else if(type == "Actor's_Name") this.actor_show = true
      else this.year_show = true
      this.searchResult.name = this.actorName
      //send request to backend/database for search result
      var url = util.format("http://localhost:8081/%s?name=%s", type, this.actorName)
      axios
        .get(url)
        .then(response =>(
          this.searchResult = response.data
          // console.log(response.data)
        ))
        .catch(err => console.log(err))
    },
    hideResult: function(){
      this.movie_show = false;
      this.actor_show = false;
      this.year_show = false;
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
