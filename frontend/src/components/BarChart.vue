<script>
import { Bar } from 'vue-chartjs'
// console.log(this.BoxofficeAnalysis)
export default {
    extends: Bar,
    // mixins: [mixins.reactiveProp],
    props: {
        barChartData: {
        type: Object,
        default: null
        },
        barChartOptions: {
        type: Object,
        default: null
        }
    },
    mounted () {
        console.log(this.barChartData)
        this.renderChart(this.barChartData, this.barChartOptions)
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
