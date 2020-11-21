<template>
  <div class="info">
    <h2>{{ searchResult.Title }} ({{searchResult.Year}})</h2>
    <b-img :src="title"></b-img>
    <h3>Actors: </h3>
    <ul>
      <li v-for="item in actors" :key="item.id">
        <h4>{{item}}</h4>
      </li>
    </ul>

    <p>{{searchResult}}</p>
  </div>
</template>

<script>
export default {
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
      title: "",
      actors:[],
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(newVal){
      this.title = newVal.Poster
      this.actors = newVal.Actors
      console.log(this.actors)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
