<template>
  <div class="info">
    <!-- <h3>{{ searchResult}})</h3> -->
    <!-- <LineChartCom v-if="barChartLoaded" :barChartData='barChartData' :barChartOptions="barChartOptions"></LineChartCom> -->
    <BarChartCom v-if="barChartLoaded" :barChartData='barChartData' :barChartOptions="barChartOptions"></BarChartCom>
    <LineChartCom v-if="comprLineChartLoaded" :lineChartData='comprLineChartData' :lineChartOptions="comprLineChartOptions"></LineChartCom>
  </div>
</template>

<script>
import LineChartCom from "./LineChart.vue"
import BarChartCom from "./BarChart.vue"
export default {
  components: { LineChartCom, BarChartCom },
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
      comprLineChartLoaded:false,
      comprLineChartData:{},
      comprLineChartOptions:{},
      barChartLoaded:false,
      barChartData:{},
      barChartOptions:{}
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(newVal){
        this.barChartData = {
            labels:[],
            datasets:[{
                label: "Thousand Dollar",
                backgroundColor: '#f87979',
                data:[]
            }]
        }
        for(var i in newVal){
            var cur = newVal[i]
            this.barChartData.labels.push(cur.Title)
            this.barChartData.datasets[0].data.push(cur.Worldwide_gross/1000)
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
        
        this.comprLineChartData = {
            labels:[],
            datasets:[
                {
                    label: "Worldwide Gross",
                    backgroundColor: 'blue',
                    yAxesGroup:'A',
                    data:[],
                    type: 'bar'
                },
                {
                    label: "IMDB Score",
                    yAxesGroup: 'B',
                    borderColor: 'yellow',
                    data:[],
                    type: 'bubble'
                }
            ]
        }
        for(var j in newVal){
            var comprCur = newVal[j]
            this.comprLineChartData.labels.push(comprCur.Title)
            this.comprLineChartData.datasets[0].data.push(comprCur.Worldwide_gross/100000000)
            this.comprLineChartData.datasets[1].data.push(comprCur.IMDB_score)
        }
        this.comprLineChartOptions = {
            scales: {
                yAxes: [{
                    id: 'A',
                    type: 'linear',
                    position: 'left',
                }, 
                {
                    id: 'score',
                    // type: 'linear',
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
        this.comprLineChartLoaded = true
    }
      

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
