import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/signup/',
    name: 'signup',
    meta: {layout: 'empty-layout'},
    component: () => import('@/views/SignUp.vue')
  },
  {
    path: '/signin/',
    name: 'signin',
    meta: {layout: 'empty-layout'},
    component: () => import('@/views/SignIn.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
