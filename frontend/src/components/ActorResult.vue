<template>
  <div class="info">
    <h3>{{ name }} </h3>
    <b-row>
        <b-col cols=2><b-img :src="img" fluid></b-img></b-col>
        <b-col>
        <b-row>
            <b-col v-for="item in know_for" :key="item.id"> 
                <b-img :src="item.Poster" fluid></b-img>
                <span>{{item.Title}} ({{item.Year}})</span>
            </b-col>
        </b-row>
        </b-col>
    </b-row>    
  </div>
</template>

<script>

export default {
  components: {  },
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
        name: "",
        imdbid: "",
        img: "",
        know_for: []
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(newVal){
      
        this.imdbid = Object.keys(newVal)[1]
        console.log(Object.keys(newVal))
        this.name = newVal[this.imdbid].Name;
        this.img = newVal[this.imdbid].Image;
        // console.log(this.name)
        this.know_for = newVal[this.imdbid].Know_for;
        console.log(this.know_for)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
