<template>
  <div class="app-container">
  <div class="login-container">
    <h2>密码登录</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">账号</label>
      <input 
        type="text" 
        id="username" 
        v-model="username" 
        placeholder="请输入账号" 
        required 
      />

      <label for="password">密码</label>
      <input 
        type="password" 
        id="password" 
        v-model="password" 
        placeholder="请输入密码" 
        required 
      />

      <button type="submit" @click="login">登录</button>
    </form>
    <p>还没有账号？<router-link to="/register">去注册</router-link></p>
    <a :href="admin_site" target="_blank" >我是管理员</a>
  </div>
</div>
</template>

<script>
import { loginUser } from '../../api/index';
import { API_BASE_URL } from '../../api/index';
import { useStore } from 'vuex';
import { ref } from 'vue';
// import { computed } from 'vue';
import { useRouter } from 'vue-router';

export default {
name: 'LoginForm',
data() {
  return {
    admin_site: API_BASE_URL+'/admin',
    // username: '',
    // password: '',
  };
},
  setup() {
    const store = useStore();
    const router = useRouter();
    const username = ref(''); // 定义响应式变量
    const password = ref('');
    // const isLoggedIn = computed(() => store.getters.isLoggedIn);
    // const username = computed(() => store.getters.getUserName);

    // const logout = () => {
    //   store.dispatch('logout');
    // };
    const handleLogin = () => {
      // 模拟登录逻辑
      loginUser(username.value, password.value).then((response) => {
        console.log(response)
        if (response.status) {
          const token=response.token;
          const username=response.username;
          // 登录成功后的处理，比如存储 token 并跳转到其他页面
          store.dispatch('login', { username, token });
          router.push('/');
        } else {
          // 登录失败的处理
        }
      })
      // 调用 Vuex 的 login action
      
    };

    return { handleLogin, username, password };
  },

methods: {},
};
</script>

<style scoped>
  .app-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #af7ce7, #709fef);
  }
  .login-container {
    width: 350px;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    animation: fadeIn 1s ease-in-out;
  }
  * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
  }
  body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background: linear-gradient(135deg, #af7ce7, #709fef);
      color: #333;
  }
  .login-container {
      width: 350px;
      padding: 40px;
      background: #fff;
      border-radius: 10px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
      animation: fadeIn 1s ease-in-out;
  }
  @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
  }
  .login-container h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
      font-size: 1.5em;
      font-weight: 700;
  }
  .login-container label {
      font-weight: 600;
      text-align:left;
      margin-top: 15px;
      display: block;
      color: #666;
  }
  .login-container input[type="text"],
  .login-container input[type="password"] {
      width: 100%;
      padding: 12px;
      margin-top: 5px;
      margin-bottom: 15px;
      border: 1px solid #ddd;
      border-radius: 6px;
      background: #f9f9f9;
      font-size: 0.9em;
      transition: background-color 0.3s ease;
  }
  .login-container input[type="text"]:focus,
  .login-container input[type="password"]:focus {
      background: #f1f1f1;
      outline: none;
      border-color: #6a11cb;
  }
  .login-container button {
      width: 100%;
      padding: 12px;
      background: linear-gradient(135deg, #6a11cb, #2575fc);
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 1em;
      font-weight: bold;
      cursor: pointer;
      transition: background 0.3s ease;
  }
  .login-container button:hover {
      background: linear-gradient(135deg, #5d0dba, #1f65d6);
  }
  .login-container p {
      text-align: center;
      margin-top: 20px;
      color: #666;
  }
  .login-container p a {
      color: #6a11cb;
      text-decoration: none;
  }
  .login-container p a:hover {
      text-decoration: underline;
  }

</style>