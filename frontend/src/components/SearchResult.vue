<template>
  <div class="info">
    <h3>{{ searchResult.Title }} ({{searchResult.Year}})</h3>
    <b-row>
    <b-col><b-img :src="searchResult.Poster" fluid></b-img></b-col>
    <b-col cols=7>
    <p>Actors: 
        <span v-for="item in searchResult.Actors" :key="item.id">{{item}} / </span> ...
    </p>
    <p>Director(s): {{searchResult.Director}}</p>
    <p>Genre: <span v-for="item in searchResult.Genre" :key="item.id"> {{item}} / </span> ...</p>
    <p>Language: {{searchResult.Language}}</p>
    <p>Run Time: {{searchResult.Runtime}}</p>
    <p>Plot: {{searchResult.Plot}}</p>
    </b-col>
    <b-col cols=3>
      <h4>Ratings: </h4>
      <p v-for="item in searchResult.Ratings" :key="item.id">  {{item.Source}}: {{item.Value}}</p>

    </b-col>
    </b-row>

    <!-- <p>{{searchResult}}</p> -->
    <b-row>
      <b-col cols=4><BarChartCom v-if="barChartLoaded" :barChartData='barChartData' :barChartOptions="barChartOptions"/></b-col>
      <b-col cols=4><PieChartCom v-if="pieChartLoaded" :pieChartData='pieChartData' :pieChartOptions="pieChartOptions"/></b-col>
      <b-col cols=4><PieChartCom v-if="domePieChartLoaded" :pieChartData='domePieChartData' :pieChartOptions="domePieChartOptions"/></b-col>
    </b-row>
    
  </div>
</template>

<script>
import BarChartCom from "./BarChart.vue"
import PieChartCom from "./PieChart.vue"
export default {
  components: { BarChartCom, PieChartCom },
  name: 'info',
  props: {
    searchResult: Object
  },
  data() {
    return {
      actors:[],
      genre: [],
      ratings: [],
      barChartLoaded:false,
      barChartData:{},
      barChartOptions:{},
      pieChartLoaded:false,
      pieChartData:{},
      pieChartOptions:{},
      domePieChartLoaded:false,
      domePieChartData:{},
      domePieChartOptions:{}
    }
  },
  methods: {
    
  },
  watch: {
    searchResult: function(newVal){
      var boAnalysis = newVal.BoxofficeAnalysis
      //海外+美国境内票房数字的柱状图
      this.barChartData = {
        labels:["Domestic","Foreign"],
        datasets:[
          {
            label: 'Thousand Dollar',
            backgroundColor: '#f87979',
            data:[boAnalysis["Domestic_Gross(dollars)"]/1000,boAnalysis["Foreign_Gross(dollars)"]/1000]
          }
        ]
      }
      this.barChartOptions = {
        title: {
          text: "Foreign vs Domestic Gross",
          fontColor: "#666",
          display: true
        },
        scales: {
          yAxes:[
            {
              ticks:  {
                max: 270000,
                min: 0
              }
            }
          ]
        },
        responsive: true,
        maintainAspectRatio: false
      }
      this.barChartLoaded = true
      //海外+美国境内票房百分比的饼图
      this.pieChartData = {
        labels:["Domestic", "Foreign"],
        datasets:[
          {
            label: 'percentage',
            backgroundColor:['#986F39', 'f87979'],
            data:[boAnalysis["Domestic_Percent"], boAnalysis["Foreign_Percent"]]
          }
        ]
      }
      this.pieChartOptions = {
        title: {
          text: "Foreign vs Domestic Gross in Percentage",
          fontColor: "#666",
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
      this.pieChartLoaded = true
      //美国境内首映票房和境内总票房的比例饼状图
      this.domePieChartData = {
        labels:["Domestic opening", "Domestic gross"],
        datasets:[
          {
            label: 'percentage',
            backgroundColor:['#986F39', 'f87979'],
            data:[
              (100 * boAnalysis["Domestic_Opening_Gross(dollars)"]/boAnalysis["Domestic_Gross(dollars)"]).toFixed(2), 
              100 - boAnalysis["Opening_Percent"]
            ]
          }
        ]
      }
      this.domePieChartOptions = {
        title: {
          text: "Domestic opening vs Domestic gross percentage",
          fontColor: "#888",
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
      this.domePieChartLoaded = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
