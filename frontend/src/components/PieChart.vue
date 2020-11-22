<script>
import { Pie } from 'vue-chartjs'
// console.log(this.BoxofficeAnalysis)
export default {
    extends: Pie,
    // mixins: [mixins.reactiveProp],
    props: {
        pieChartData: {
            type: Object,
            default: null
        },
        pieChartOptions: {
            type: Object,
            default: null
        }
    },
    mounted () {
        console.log(this.pieChartData)
        this.renderChart(this.pieChartData, this.pieChartOptions)
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>