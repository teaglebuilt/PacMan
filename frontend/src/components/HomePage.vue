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
            <ul v-if="errors && errors.length">
              <li v-for="error of errors">
                  {{error.message}}
              </li>
          </ul>
        </div>
        <div>
        <ul v-for="(key, val) in response">
          <li :class="{ activeclass: key.isActive }">
            <div class="flex justify-content justify-around mb-4 items-center border border-gray-500 shadow p-4 m-4">
              <span class="flex-1 font-medium font-mono pr-6 text-grey-darkest text-left">
                <p class="border ">{{ val }}</p>
              </span>
                <div v-for="(element, index ) in key" :key="index" class="flex-col flex-2">
                   <span v-if="index == 'get'" class="border border-green-400 p-2 rounded relative bg-green-600 text-white">{{ index }}</span>
                   <span v-if="index == 'delete'" class="border border-red-light text-red-dark p-2 rounded relative bg-red-500 text-white">{{ index }}</span>
                   <span v-if="index == 'post'" class="border border-blue-light p-2 rounded relative bg-blue-500 text-white">{{ index }}</span>
                   <span v-if="index == 'put'" class="border border-purple-500 bg-purple-600 p-2 rounded relative text-white">{{ index }}</span>
                </div>
              <button @click="toggle(key)" class="flex-3 pl-2">Open</button>
            </div>
            <div v-show="key.isActive" class="mt-1 mb-10 ml-2">
                  <div class="w-full flex bg-white flex justify-center">
                    <div class="custom-number-input h-10 w-32 ml-4">
                       <label for="custom-input-number" class="w-full text-gray-700 text-sm font-semibold ml-3">
                       Requests
                       </label>
                       <div class="flex flex-row h-8 w-2/3 rounded-lg relative bg-transparent ml-2 mt-1 bg-gray-400">
                          <a v-on:click="requests -= 1"class="text-gray-600 hover:text-gray-700 hover:bg-gray-400 h-full w-10 rounded-l cursor-pointer outline-none">
                             <span class="m-auto text-2xl font-thin pl-2">−</span>
                          </a>
                            {{ requests }}
                          <a v-on:click="requests += 1" class="text-gray-600 hover:text-gray-700 hover:bg-gray-400 h-full w-10 rounded-r cursor-pointer">
                            <span class="m-auto text-xl font-thin pr-2 float-right">+</span>
                          </a>
                       </div>
                    </div>
                    <div class="h-10 w-32 ml-4">
                       <label class="w-full text-gray-700 text-sm font-semibold">
                       Concurrency
                       </label>
                       <div class="flex flex-row h-8 w-2/3 rounded-lg relative bg-transparent mt-1 bg-gray-400">
                          <a v-on:click="concurrency -= 1" class="text-gray-600 h-full w-10 outline-none pl-2">
                             <span class="m-auto text-2xl font-thin">−</span>
                          </a>
                          {{ concurrency }}
                          <a @click="concurrency += 1" class="text-gray-600 h-full w-10 cursor-pointer">
                            <span class="m-auto text-xl font-thin float-right pr-2">+</span>
                          </a>
                       </div>
                    </div>
                    <div class="flex mt-5">
                      <div class="mx-2">
                        <button @click="executeTest(val)"
                          class="w-32 bg-white tracking-wide text-gray-800 font-bold rounded border-b-2 border-blue-500 hover:border-blue-600 hover:bg-blue-500 hover:text-white shadow-md py-2 px-6 inline-flex items-center">
                          <span class="mx-auto">Start</span>
                        </button>
                      </div>
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

export default {
  mounted() {
    console.log(process.env)
  },
  data () {
    return {
      host: "",
      isOpen: false,
      requests: 1,
      concurrency: 1,
      response: ""
    }
  },
  methods: {
    handleSubmit() {
      this.host = this.api_uri
      axios.post(`${process.env.VUE_APP_API_URL}/endpoints`, {
        body: this.api_uri
      })
    .then(response => {
      let dictionary = response.data.endpoints;
      Object.keys(dictionary).forEach(function(key) { 
          dictionary[key]["isActive"] = false;
        });
        this.response = dictionary
    })
    .catch(e => {
      console.log(e)
      this.errors.push(e)
    })
    },
    toggle: function (item) {
        item.isActive = !item.isActive;
    },
    decrement: function (e) {
      console.log(e.target.value)
    },
    executeTest: function (endpoint) {
        console.log(endpoint, this.requests, this.concurrency)
        axios.post(`${process.env.VUE_APP_API_URL}/load_test`, {
          url: `https://petstore.swagger.io/v2` + endpoint + `/` + `1`,
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
