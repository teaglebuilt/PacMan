<template>
  <div class="bg-gray-200">
    <nav id="header" class="bg-white w-full z-10 top-0 shadow mb-10 py-2">
      <div class="w-full container mx-auto flex flex-wrap items-center mt-0 pt-3 pb-3 md:pb-0">
        <div class="w-1/2 pl-2 md:pl-0">
			  	<a class="text-gray-900 text-base xl:text-xl no-underline hover:no-underline font-bold"  href="#"> 
					  <i class="fas fa-sun text-orange-600 pr-3"></i> Pac Man
				  </a>
        </div>
          <div class="w-full flex-grow lg:flex lg:items-center lg:w-auto hidden lg:block mt-2 lg:mt-0 bg-white z-20" id="nav-content">
                <ul class="list-reset lg:flex flex-1 items-center px-4 md:px-0">
                  <li class="mr-6 my-2 md:my-0">
                    <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-orange-600 no-underline hover:text-gray-900 border-b-2 border-orange-600 hover:border-orange-600">
                        <i class="fas fa-home fa-fw mr-3 text-orange-600"></i><span class="pb-1 md:pb-0 text-sm">Home</span>
                      </a>
                  </li>
                  <li class="mr-6 my-2 md:my-0">
                    <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-900 border-b-2 border-white hover:border-pink-500">
                        <i class="fas fa-tasks fa-fw mr-3"></i><span class="pb-1 md:pb-0 text-sm">Tasks</span>
                      </a>
                  </li>
                  <li class="mr-6 my-2 md:my-0">
                      <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-900 border-b-2 border-white hover:border-purple-500">
                        <i class="fa fa-envelope fa-fw mr-3"></i><span class="pb-1 md:pb-0 text-sm">Messages</span>
                      </a>
                  </li>
                  <li class="mr-6 my-2 md:my-0">
                      <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-900 border-b-2 border-white hover:border-green-500">
                          <i class="fas fa-chart-area fa-fw mr-3"></i><span class="pb-1 md:pb-0 text-sm">Analytics</span>
                      </a>
                  </li>
                  <li class="mr-6 my-2 md:my-0">
                      <a href="#" class="block py-1 md:py-3 pl-1 align-middle text-gray-500 no-underline hover:text-gray-900 border-b-2 border-white hover:border-red-500">
                        <i class="fa fa-wallet fa-fw mr-3"></i><span class="pb-1 md:pb-0 text-sm">Payments</span>
                      </a>
                </li>
              </ul>
          </div>
      </div>
    </nav>
    <div class="container w-full mx-auto">
      <div class="w-full px-4 md:px-0 md:mt-8 mb-16 text-gray-800 leading-normal">
        <div class="flex flex-row flex-wrap justify-between">
          <div class="w-1/2">
            <HomePage />
          </div>
          <div class="w-1/2">
            <Chart />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'
import Chart from './components/Chart.vue'


export default {
  name: 'app',
  components: {
    HomePage,
    Chart
  }
}
</script>


