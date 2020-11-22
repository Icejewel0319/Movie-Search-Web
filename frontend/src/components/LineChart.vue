<script>
import { Line } from 'vue-chartjs'
// console.log(this.BoxofficeAnalysis)
export default {
    extends: Line,
    // mixins: [mixins.reactiveProp],
    props: {
        lineChartData: {
        type: Object,
        default: null
        },
        lineChartOptions: {
        type: Object,
        default: null
        }
    },
    mounted () {
        console.log(this.lineChartData)
        this.renderChart(this.lineChartData, this.lineChartOptions)
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>