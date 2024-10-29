import { createRouter, createWebHistory } from 'vue-router';
import LoginForm  from './views/LoginForm .vue';

const routes = [
  { path: '/login', component: LoginForm  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;