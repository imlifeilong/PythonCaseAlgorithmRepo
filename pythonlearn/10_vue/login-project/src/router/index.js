import { createRouter, createWebHistory } from 'vue-router';
import LoginForm  from './views/LoginForm .vue';
import RegisterFrom from './views/RegisterFrom.vue';

const routes = [
  { path: '/login', component: LoginForm  },
  { path: '/register', component: RegisterFrom },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;