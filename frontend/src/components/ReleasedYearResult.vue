<template>
  <div class="info">
    <!-- <h3>{{ searchResult}})</h3> -->
    <LineChartCom v-if="lineChartLoaded" :lineChartData='lineChartData' :lineChartOptions="lineChartOptions"></LineChartCom>
    <LineChartCom v-if="comprLineChartLoaded" :lineChartData='comprLineChartData' :lineChartOptions="comprLineChartOptions"></LineChartCom>
    
  </div>
</template>

<script>
import LineChartCom from "./LineChart.vue"
export default {
  components: { LineChartCom },
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
      
      comprLineChartLoaded:false,
      comprLineChartData:{},
      comprLineChartOptions:{},
      lineChartLoaded:false,
      lineChartData:{},
      lineChartOptions:{}
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(newVal){
        this.lineChartData = {
            labels:[],
            datasets:[{
                label: "Thousand Dollar",
                backgroundColor: '#f87979',
                data:[]
            }]
        }
        for(var i in newVal){
            var cur = newVal[i]
            this.lineChartData.labels.push(cur.Title)
            this.lineChartData.datasets[0].data.push(cur.Worldwide_gross/1000)
        }
        this.lineChartOptions = {
            title: {
                text: "Top 10 Movie with Max Gross",
                fontColor: "#666",
                display: true
            },
            responsive: true,
            maintainAspectRatio: false
        }
        this.lineChartLoaded = true
        
        this.comprLineChartData = {
            labels:[],
            datasets:[
                {
                    label: "Rank",
                    borderColor: 'blue',
                    yAxesGroup:'A',
                    data:[]
                },
                {
                    label: "IMDB Score",
                    yAxesGroup: 'B',
                    borderColor: 'red',
                    data:[]
                }
            ]
        }
        for(var j in newVal){
            var comprCur = newVal[j]
            this.comprLineChartData.labels.push(comprCur.Title)
            this.comprLineChartData.datasets[0].data.push(comprCur.Rank)
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
                    id: 'B',
                    type: 'linear',
                    position: 'right',
                    ticks: {
                        max: 10,
                        min: 0,
                        reverse: true
                    },
                }]
            },
            title: {
                text: "Rankings and IMDB Scores for Top 10 Movies",
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
