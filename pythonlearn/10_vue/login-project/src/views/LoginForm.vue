<template>
  <div class="app-container">
  <div class="login-container">
    <h2>Welcome Back</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">Username</label>
      <input 
        type="text" 
        id="username" 
        v-model="username" 
        placeholder="Enter your username" 
        required 
      />

      <label for="password">Password</label>
      <input 
        type="password" 
        id="password" 
        v-model="password" 
        placeholder="Enter your password" 
        required 
      />

      <button type="submit" @click="login">Login</button>
    </form>
    <p>还没有账号？<a href="/api/register/">立即注册</a></p>
  </div>
</div>
</template>

<script>
import { loginUser } from '../api/index';
export default {
data() {
  return {
    username: '',
    password: '',
  };
},
methods: {
  login() {
    const { username, password } = this;
    loginUser(username, password)
     .then((response) => {
        if (response.success) {
          // 登录成功后的处理，比如存储 token 并跳转到其他页面
        } else {
          // 登录失败的处理
        }
      })
     .catch((error) => {
        // 处理错误情况
        console.error('登录错误：', error);
      });
  },
},
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