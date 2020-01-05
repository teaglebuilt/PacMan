<template>
    <div>
        <h2 class="font-bold text-center mb-4">{{ endpoint.summary }}</h2>

        <h4 class="font-semibold font-mono">Parameters</h4>
        <input type="number" v-if="endpoint.parameters.type == 'integer'" />
        <div v-else-if="endpoint.parameters.length > 1">
            <form @submit.prevent="executeTest()">
                <div v-for="(param, index) in endpoint.parameters" :key="index">
                    <h5 class="text-red-600">Required: {{ param.required }}</h5>
                    <p>{{ param.description }}</p>
                    <span class="font-mono font-semibold px-1">{{param.name}}</span>
                    <input v-if="param.type == 'string'" v-model="parameter" type="string" class="border border-gray-400 p-1 m-2 w-3/4" />
                    <input v-else-if="param.type == 'integer'" v-model="parameter" type="number" class="border border-gray-400 p-1 m-2 w-1/2" />
                    <textarea v-else-if="param.in == 'body'" v-model="parameter" rows="6" class="resize border border-gray-500 rounded focus:shadow-outline mt-1 w-full">
                        {}
                    </textarea>
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
        <div v-else class="mb-2" v-for="(key, index) in endpoint.parameters" :key="index">
            <p class="p-1"><span class="font-semibold">Description: </span>{{ key["description"] }}</p>
            <div v-if="key.collectionFormat == 'multi'" v-bind:options="key.items.enum">
                <form @submit.prevent="executeOptions()">
                    <multiselect
                        v-model="selected"
                        :options="options"
                        @select="onSelect"
                        >
                    </multiselect>
                    <button type="submit">Submit</button>
                </form>
            </div>
            <!-- <p class="p-1"><span class="font-semibold">Schema:</span>{{ key["format"] }}</p>
            <p class="p-1"><span class="font-semibold">Schema:</span>{{ key["body"] }}</p> -->
        </div>
        <h4 class="font-semibold font-mono">Responses</h4>
        <div class="border border-gray-400 bor" v-for="(key, val) in endpoint.responses" :key="val">
            <p class="p-1"><span class="font-semibold px-2">{{ val }}: </span>{{ key["description"] }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Multiselect from 'vue-multiselect'

export default {
    props: {
        endpoint: {
            type: Object,
            required: true
        },
        host: {
            type: String,
            required: true
        },
        address: {
            type: String,
            required: true
        }
    },
    components: { Multiselect },
    data() {
        return {
            selected: null,
            options: [],
            parameter: ""
        }
    },
    methods: {
        executeTest: function () {
        console.log(this.parameter, this.host, this.address)
        axios.post(`${process.env.VUE_APP_API_URL}/load_test`, {
          url: `${this.host}/${this.address}`,
          data: this.parameter,
          requests: 2,
          concurrency: 4
        }).then(res => {
          console.log(res)
          this.$root.$emit('fillData', res)
        }).catch(e => {
      console.log(e)
      })
    },
    executeOptions() {
        console.log(this.options)
        axios.post(`${process.env.VUE_APP_API_URL}/load_test`, {
          url: `${this.host}/${this.address}`,
          data: this.options,
          requests: 2,
          concurrency: 4
        }).then(res => {
          console.log(res)
          this.$root.$emit('fillData', res)
        }).catch(e => {
        console.log(e)
      })
    },
    onSelect (option) {
        console.log(option)
        this.options.push(option)
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>