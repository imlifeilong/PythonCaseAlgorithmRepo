<template>
  <div id="app">
    <div v-if="!isLoggedIn">
      <LoginForm />
    </div>
    <div v-else>
      <!-- �ѵ�¼״̬����ʾ������ -->
      <h2>��ӭ���ѵ�¼�û���</h2>
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
      isLoggedIn: false, // ��ʼ״̬Ϊδ��¼
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