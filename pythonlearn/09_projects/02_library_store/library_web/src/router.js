import { createRouter, createWebHistory } from 'vue-router';
import LoginForm  from './components/views/LoginForm.vue';
import RegisterForm from './components/views/RegisterForm.vue';
import SlideShow from './components/views/SlideShow.vue';

const routes = [
  { path: '/login', component: LoginForm  },
  { path: '/register', component: RegisterForm },
  { path: '/', component:SlideShow }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;