import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import VueRouter from 'vue-router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueRouter)

Vue.config.productionTip = false

// import MemberCom from './components/Member.vue'

const appRouter = new VueRouter({
  // routes 选项用来配置路由表
  // 当请求 /xxx 的时候，渲染 xxx 组件
  // routes 是一个数组，数组中存储一些固定格式的对象
  // 对象 path 表示请求的路径
  // 对象的 component 用来指定当你请求 path 路径的时候，渲染该组件
  // 现在的问题是？匹配到 path 的时候，组件往哪里渲染？
  // 在你的根组件预留一个路由的出口，用来告诉路由到匹配到某个 path 的时候，把该组件渲染到哪里
  routes: [
    {
      path: '/member',
      component: {
        template: `<div>member</div>`
      }
    },
    {
      path: '/bar',
      component: {
        template: `<div>bar 组件啊</div>`
      }
    }
  ]
})

new Vue({
  render: h => h(App),
  router: appRouter,
}).$mount('#app')
