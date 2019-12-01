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
        this.datacollection = {
          labels: ["slowest"],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [res.data.average]
            },
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [res.data.slowest]
            }
          ]
        }
      })
    },
    methods: {
      fillData () {
        console.log("poop")
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }
    }
  }
</script>

<style>
</style>