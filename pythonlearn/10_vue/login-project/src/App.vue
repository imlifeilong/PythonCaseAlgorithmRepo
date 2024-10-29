<template>
  <div id="app">
    <div v-if="!isLoggedIn">
      <LoginForm />
    </div>
    <div v-else>
      <!-- 已登录状态下显示的内容 -->
      <h2>欢迎，已登录用户！</h2>
    </div>
  </div>
</template>

<script>
import LoginForm from './views/LoginForm.vue';

export default {
  name: 'App',
  components: {
    LoginForm,
  },
  data() {
    return {
      isLoggedIn: false, // 初始状态为未登录
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>