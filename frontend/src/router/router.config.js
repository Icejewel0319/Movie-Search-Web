import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
    // routes 选项用来配置路由表
    routes: [
    {
        path: '/',
        name: 'Actor',
        component: (resolve) => require(['../components/SearchActor.vue'],resolve)
        },
    {
        path: '/member',
        name: 'Member',
        component: (resolve) => require(['../components/Member.vue'],resolve)
    },
    {
        path: '/searchActor',
        name: 'Actor',
        component: (resolve) => require(['../components/SearchActor.vue'],resolve)
    },
    {
        path: '/searchMovie',
        name: 'Movie',
        component: (resolve) => require(['../components/SearchMovie.vue'],resolve)
    },
    {
        path: '/searchYear',
        name: 'ReleasedYear',
        component: (resolve) => require(['../components/SearchYear.vue'],resolve)
    }
    ]
  })

export default router
  