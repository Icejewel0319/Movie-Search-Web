<template>
  <div class="search container">
    <h2>Search by Released Year!</h2>
    <b-row>
    <b-col><b-form-input v-model="input" placeholder="Enter Released Year"></b-form-input></b-col>
    <b-col lg="2"><b-button @click="search" pill variant="outline-success">search <b-icon icon="search"></b-icon></b-button></b-col>
    </b-row>
    <!-- <b-alert show variant="warning">Warning Alert</b-alert> -->
    <b-alert show variant="warning" v-if="not_number">Input should be a number!</b-alert>
    <YearResultCom v-if="show" :searchResult="searchResult"/>
  </div>
</template>

<script>
// import SearchResultCom from './SearchResult.vue'
import YearResultCom from './ReleasedYearResult.vue'
const axios = require('axios'),
      util  = require('util');

export default {
  components: { YearResultCom },
  name: 'search',
  props: {
    msg: String
  },
  data() {
    return {
      input: "",
      show: false,
      not_number: false,
      searchResult: {}
    }
  },
  methods: {
    search: function(){
      var type = "Released_Year"
      var reg_exp = /^[0-9]+.?[0-9]*/
      console.log(type);
      if(!reg_exp.test(this.input)){
          this.not_number = true
          this.show = false
      } else {
        this.not_number = false
        var url = util.format("http://localhost:8081/%s?input=%s", type, this.input)
        axios
            .get(url)
            .then((response) =>{
            this.searchResult = response.data
            this.show = true
            })
            .catch(err => console.log(err))
      }
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
