<template>
  <div class="app-container">
  <div class="register-container">
    <h2>注册</h2>
    <form @submit.prevent="handleLogin">
      <label for="username">账号</label>
      <input 
        type="text" 
        id="username" 
        v-model="username" 
        placeholder="请输入账号\手机号\邮箱" 
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

      <label for="confirmpassword">确认密码</label>
      <input 
        type="password" 
        id="confirmpassword" 
        v-model="confirmpassword" 
        placeholder="请再次输入密码" 
        required 
      />

      <button type="submit" @click="register">注册</button>
    </form>
    <p>已有账号？<router-link to="/login">去登录</router-link></p>
  </div>
</div>
</template>

<script>
import { registerUser } from '../../api/index';
export default {
  name: 'RegisterForm',
data() {
  return {
    username: '',
    password: '',
    confirmpassword: '',
  };
},
methods: {
  register() {
        if (this.password === this.confirmpassword) {
          const { username, password } = this;
          registerUser(username, password)
           .then((response) => {
              if (response.success) {
                // 注册成功后的处理，例如提示用户并可能跳转到登录页面
                alert('注册成功，请登录！');
                this.$router.push('/login'); // 跳转到登录页面
              } else {
                // 注册失败的处理，例如显示错误消息
                alert('服务器处理错误，请重新提交！');
              }
            })
           .catch((error) => {
              console.error('注册错误：', error);
              alert('注册失败，请重新提交！');
            });
        } else {
          // 密码不一致的处理，例如显示提示信息
          alert('密码不一致，请重新输入');
        }
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
  .register-container {
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
  .register-container {
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
  .register-container h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
      font-size: 1.5em;
      font-weight: 700;
  }
  .register-container label {
      font-weight: 600;
      text-align:left;
      margin-top: 15px;
      display: block;
      color: #666;
  }
  .register-container input[type="text"],
  .register-container input[type="confirmpassword"],
  .register-container input[type="password"] {
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
  .register-container input[type="text"]:focus,
  .register-container input[type="confirmpassword"]:focus,
  .register-container input[type="password"]:focus {
      background: #f1f1f1;
      outline: none;
      border-color: #6a11cb;
  }
  .register-container button {
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
  .register-container button:hover {
      background: linear-gradient(135deg, #5d0dba, #1f65d6);
  }
  .register-container p {
      text-align: center;
      margin-top: 20px;
      color: #666;
  }
  .register-container p a {
      color: #6a11cb;
      text-decoration: none;
  }
  .register-container p a:hover {
      text-decoration: underline;
  }

</style>