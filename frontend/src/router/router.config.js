import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
    // routes 选项用来配置路由表
    routes: [
      {
        path: '/member',
        name: 'Member',
        component: (resolve) => require(['../components/Member.vue'],resolve)
      },
      {
        path: '/search',
        component: (resolve) => require(['../components/Search.vue'],resolve)
      }
    ]
  })

export default router
  