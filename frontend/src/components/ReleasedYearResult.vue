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
            // if(cur.Worldwide_gross){
            this.lineChartData.datasets[0].data.push(cur.Worldwide_gross/1000)
            // } else if (cur["Worldwide_gross(dollar)"]){
            //     this.lineChartData.datasets[0].data.push(cur["Worldwide_gross(dollar)"]/1000)
            // }       
        }
        this.lineChartOptions = {
            title: {
                text: "Top 10 Movie",
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
                    label: "Thousand Dollar",
                    backgroundColor: '#f87979',
                    data:[]
                },
                {
                    label: "Ranking",
                    backgroundColor: 'red',
                    data:[]
                }
            ]
        }
        for(var j in newVal){
            var comprCur = newVal[j]
            this.comprLineChartData.labels.push(comprCur.Title)
            // if(cur.Worldwide_gross){
            this.comprLineChartData.datasets[0].data.push(comprCur.Worldwide_gross/1000)
            this.comprLineChartData.datasets[1].data.push(comprCur.IMDB_score)
            // } else if (cur["Worldwide_gross(dollar)"]){
            //     this.lineChartData.datasets[0].data.push(cur["Worldwide_gross(dollar)"]/1000)
            // }       
        }
        this.comprLineChartOptions = {
            title: {
                text: "Top 10 Movie",
                fontColor: "#999",
                display: true
            },
            responsive: true,
            maintainAspectRatio: false
        }
        this.comprLineChartLoaded = true
    }
      

    //   var boAnalysis = newVal.BoxofficeAnalysis
    //   //海外+美国境内票房数字的柱状图
    //   this.barChartData = {
    //     labels:["Domestic","Foreign"],
    //     datasets:[
    //       {
    //         label: 'dollar',
    //         backgroundColor: '#f87979',
    //         data:[boAnalysis["Domestic_Gross(dollars)"],boAnalysis["Foreign_Gross(dollars)"]]
    //       }
    //     ]
    //   }
    //   this.barChartOptions = {
    //     title: {
    //       text: "hahahah",
    //       fontColor: "#666",
    //       display: true
    //     },
    //     responsive: true,
    //     maintainAspectRatio: false
    //   }
    //   this.barChartLoaded = true
    //   //海外+美国境内票房百分比的饼图
    //   this.pieChartData = {
    //     labels:["Domestic", "Foreign"],
    //     datasets:[
    //       {
    //         label: 'percentage',
    //         backgroundColor:['#986F39', 'f87979'],
    //         data:[boAnalysis["Domestic_Percent"], boAnalysis["Foreign_Percent"]]
    //       }
    //     ]
    //   }
    //   this.pieChartOptions = {
    //     title: {
    //       text: "hahahah",
    //       fontColor: "#666",
    //       display: true
    //     },
    //     responsive: true,
    //     maintainAspectRatio: false
    //   }
    //   this.pieChartLoaded = true
    //   //美国境内首映票房和境内总票房的比例饼状图
    //   this.domePieChartData = {
    //     labels:["Domestic", "Foreign"],
    //     datasets:[
    //       {
    //         label: 'percentage',
    //         backgroundColor:['#986F39', 'f87979'],
    //         data:[
    //           (100 * boAnalysis["Domestic_Opening_Gross(dollars)"]/boAnalysis["Domestic_Gross(dollars)"]).toFixed(2), 
    //           100 - boAnalysis["Opening_Percent"]
    //         ]
    //       }
    //     ]
    //   }
    //   this.domePieChartOptions = {
    //     title: {
    //       text: "Domestic opening vs Domestic gross",
    //       fontColor: "#888",
    //       display: true
    //     },
    //     responsive: true,
    //     maintainAspectRatio: false
    //   }
    //   this.domePieChartLoaded = true
    // }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
