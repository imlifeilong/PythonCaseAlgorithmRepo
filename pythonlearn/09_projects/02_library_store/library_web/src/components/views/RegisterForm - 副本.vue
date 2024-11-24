<template>
    <div class="register-container">
      <h2 class="register-title">注册</h2>
      <div class="input-group">
        <label for="username">用户名</label>
        <input type="text" v-model="username" id="username" placeholder="请输入用户名" />
      </div>
      <div class="input-group">
        <label for="password">密码</label>
        <input type="password" v-model="password" id="password" placeholder="请输入密码" />
      </div>
      <div class="input-group">
        <label for="confirmpassword">确认密码</label>
        <input type="password" v-model="confirmpassword" id="confirmpassword" placeholder="请再次输入密码" />
      </div>
      <button class="register-button" @click="register">注册</button>
      <p>已有账号？<router-link to="/login">去登录</router-link></p>
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
  .register-container {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .register-title {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
  }
  
  .input-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    font-size: 14px;
    color: #666;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .register-button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .register-button:hover {
    background-color: #45a049;
  }
  </style>