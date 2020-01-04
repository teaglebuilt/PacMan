<template>
  <div class="small">
    <line-chart :chart-data="datacollection"></line-chart>
  </div>
</template>

<script>
import LineChart from './LineChart.js'

export default {
  components: {
    LineChart
  },
  data () {
    return {
      loaded: false,
      datacollection: null
    }
  },
  mounted () {
    this.$root.$on('fillData', (res) => {
      console.log(res.data.objects.map(obj => obj.request_time))
      this.datacollection = {
          datasets: [
            {
              label: 'Slowest to Fastest',
              backgroundColor: '#f87979',
              data: res.data.objects.map(obj => obj.request_time)
            }
          ]
        }
      })
    }
  }
</script>
