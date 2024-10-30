<template>
    <div class="register-container">
      <h2 class="register-title">注册</h2>
      <div class="input-group">
        <label for="registerUsername">用户名</label>
        <input type="text" v-model="registerUsername" id="registerUsername" placeholder="请输入用户名" />
      </div>
      <div class="input-group">
        <label for="registerPassword">密码</label>
        <input type="password" v-model="registerPassword" id="registerPassword" placeholder="请输入密码" />
      </div>
      <div class="input-group">
        <label for="confirmPassword">确认密码</label>
        <input type="password" v-model="confirmPassword" id="confirmPassword" placeholder="请再次输入密码" />
      </div>
      <button class="register-button" @click="register">注册</button>
    </div>
  </template>
  
  <script>
  import { registerUser } from '../services/authService';
  
  export default {
    name: 'Register',
    data() {
      return {
        registerUsername: '',
        registerPassword: '',
        confirmPassword: '',
      };
    },
    methods: {
      register() {
        if (this.registerPassword === this.confirmPassword) {
          const { registerUsername, registerPassword } = this;
          registerUser(registerUsername, registerPassword)
           .then((response) => {
              if (response.success) {
                // 注册成功后的处理，例如提示用户并可能跳转到登录页面
              } else {
                // 注册失败的处理，例如显示错误消息
              }
            })
           .catch((error) => {
              console.error('注册错误：', error);
            });
        } else {
          // 密码不一致的处理，例如显示提示信息
          console.error('密码不一致，请重新输入');
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