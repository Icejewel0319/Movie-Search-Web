<template>
  <div class="info">
    <!-- <h3>{{ searchResult}})</h3> -->
    <!-- <LineChartCom v-if="barChartLoaded" :barChartData='barChartData' :barChartOptions="barChartOptions"></LineChartCom> -->
    <BarChartCom v-if="barChartLoaded" :barChartData='barChartData' :barChartOptions="barChartOptions"></BarChartCom>
    <BarChartCom v-if="comprBarChartLoaded" :barChartData='comprBarChartData' :barChartOptions="comprBarChartOptions"></BarChartCom>
  </div>
</template>

<script>
// import LineChartCom from "./LineChart.vue"
import BarChartCom from "./BarChart.vue"
export default {
  components: { 
    //   LineChartCom, 
      BarChartCom 
    },
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
      comprBarChartLoaded:false,
      comprBarChartData:{},
      comprBarChartOptions:{},
      barChartLoaded:false,
      barChartData:{},
      barChartOptions:{}
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(new_value){
        var year = Object.keys(new_value)[0]
        var newVal = new_value[year]
        this.barChartData = {
            labels:[],
            datasets:[
                {
                    label: "Domestic Gross (Thousand Dollars)",
                    backgroundColor: 'rgb(141,165,208)',
                    data:[]
                },
                {
                    label: "Worldwide Gross (Thousand Dollars)",
                    backgroundColor: 'rgb(229,122,15)',
                    data:[]
                }
            ]
        }
        for(var i in newVal){
            var cur = newVal[i]
            this.barChartData.labels.push(cur.title)
            this.barChartData.datasets[0].data.push(cur["Domestic_Gross(dollars)"]/1000)
            this.barChartData.datasets[1].data.push(cur["Worldwide_Gross(dollars)"]/1000)
        }
        this.barChartOptions = {
            title: {
                text: "Top 10 Movie with Highest Gross",
                fontColor: "#666",
                display: true
            },
            scales: {
                yAxes: [{
                    ticks: {beginAtZero: true}
                }]
            },
            responsive: true,
            maintainAspectRatio: false
        }
        this.barChartLoaded = true
        
        this.comprBarChartData = {
            labels:[],
            datasets:[
                {
                    label: "Worldwide Gross (Thousand Dollars)",
                    fillColor: 'rgb(229,122,15)',
                    yAxisID:'gross',
                    data:[],
                    type: 'bar'
                },
                {
                    label: "IMDB Score",
                    yAxisID: 'score',
                    borderColor: 'red',
                    data:[],
                    type: 'bubble'
                }
            ]
        }
        for(var j in newVal){
            var comprCur = newVal[j]
            this.comprBarChartData.labels.push(comprCur.title)
            this.comprBarChartData.datasets[0].data.push(comprCur["Worldwide_Gross(dollars)"]/1000)
            this.comprBarChartData.datasets[1].data.push(comprCur["imdb_score"])
        }
        this.comprBarChartOptions = {
            scales: {
                yAxes: [{
                    id: 'gross',
                    // type: 'linear',
                    position: 'left',
                    ticks: {
                        min: 0
                    }
                }, 
                {
                    id: 'score',
                    type: 'linear',
                    position: 'right',
                    ticks: {
                        max: 10,
                        min: 0
                        // reverse: true
                    },
                }]
            },
            title: {
                text: "Box Office and IMDB Scores for the Top 10 Movies",
                fontColor: "#999",
                display: true
            },
            responsive: true,
            maintainAspectRatio: false
        }
        this.comprBarChartLoaded = true
    }
      

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
