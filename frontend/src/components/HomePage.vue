<template>
<div class="h-100 w-full flex items-center justify-center bg-teal-lightest font-sans">
	<div class="bg-white rounded shadow p-6 m-4 w-full lg:w-3/4 lg:max-w-lg">
        <div class="mb-4">
            <h1 class="text-grey-darkest font-semibold">Load Swagger</h1>
            <span class="text-left text-sm font-light italic">url ending in swagger.json</span>
            <form @submit.prevent="handleSubmit()" class="flex mt-4">
                <input type="url" v-model="api_uri" class="shadow border rounded py-2 px-3 text-grey-darker w-full">
                <button type="submit" class="flex-no-shrink p-2 border-2 rounded text-teal border-teal hover:text-white hover:bg-teal">Load</button>
            </form>
            <!-- <ul v-if="errors && errors.length">
              <li v-for="error of errors">
                  {{error.message}}
              </li>
          </ul> -->
        </div>
        <div>
        <ul v-for="(key, val) in response" :key="key.operationId">
          <li :class="{ activeclass: key.isActive }">
            <div class="flex justify-content justify-around mb-4 items-center border border-gray-500 shadow p-4 m-4">
              <span class="flex-1 font-medium font-mono pr-6 text-grey-darkest text-left">
                <p class="border">{{ val }}</p>
              </span>
                
              <button @click="toggle(key, val)" class="flex-3 pl-2">Open</button>
            </div>
            <div v-show="key.isActive" class="mt-1 mb-10 ml-2">
                  <div v-for="(element, index ) in key" :key="index" class="flex-col flex-2">
                    <button @click="toggledata(element, index)" v-if="index == 'get'" class="border border-green-400 p-2 rounded relative bg-green-600 text-white">{{ index }}</button>
                    <button @click="toggledata(element, index)" v-else-if="index == 'delete'" class="border border-red-light text-red-dark p-2 rounded relative bg-red-500 text-white">{{ index }}</button>
                    <button @click="toggledata(element, index)" v-else-if="index == 'post'" class="border border-purple-500 bg-green-600 p-2 rounded relative text-white">{{ index }}</button>
                    <button @click="toggledata(element, index)" v-else-if="index == 'put'" class="border border-purple-500 bg-purple-600 p-2 rounded relative text-white">{{ index }}</button>
                  </div>
                  <div v-show="endpoint.open" class="flex flex-row">
                     <div class="flex flex-col">
                        <Endpoint :address="endpoint_addr" :host="api_uri" :endpoint="endpoint" />
                      </div>
                  </div>
            </div>
          </li>
       </ul>
    </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'
import Endpoint from './Endpoint.vue'


export default {
  components: {
    Endpoint
  },
  data () {
    return {
      api_uri: "https://petstore.swagger.io/v2/swagger.json",
      requests: 1,
      concurrency: 1,
      response: "",
      endpoint_addr: "",
      endpoint: {
        consumes: [],
        description: "",
        parameters: [],
        produces: [],
        responses: {},
        security: [],
        summary: "",
        open: false
      }
    }
  },
  methods: {
    handleSubmit() {
      axios.post(`${process.env.VUE_APP_API_URL}/endpoints`, {
        body: this.api_uri
      })
    .then(response => {
      console.log(response)
      let dictionary = response.data.endpoints;
      Object.keys(dictionary).forEach(function(key) { 
          dictionary[key]["isActive"] = false;
          Object.entries(dictionary[key]).forEach(([key, value]) => {
            if(value === false){
              return false
            }
            else {
              value["open"] = false
            }
          });
        });
        this.response = dictionary
    })
    .catch(e => {
      console.log(e)
      this.errors.push(e)
    })
    },
    toggledata(e, i){
      console.log(e, i)
      this.endpoint.consumes = e.consumes
      this.endpoint.description = e.description
      this.endpoint.parameters = e.parameters
      this.endpoint.produces = e.produces
      this.endpoint.responses = e.responses
      this.endpoint.security = e.security
      this.endpoint.summary = e.summary
      this.endpoint.open = e.open
      e.open = !e.open
    },
    toggle: function (item, addr) {
      item.isActive = !item.isActive;
      this.endpoint_addr = addr
    },
    executeTest: function (endpoint) {
        console.log(endpoint, this.requests, this.concurrency)
        axios.post(`${process.env.VUE_APP_API_URL}/load_test`, {
          url: `${this.host}/${endpoint}/${params}`,
          requests: this.requests,
          concurrency: this.concurrency
        }).then(res => {
          console.log(res)
          this.$root.$emit('fillData', res)
        }).catch(e => {
      console.log(e)
      })
    }
  }
}
</script>
