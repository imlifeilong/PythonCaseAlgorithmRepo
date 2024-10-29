<template>
    <div class="login-container">
      <h2 class="login-title">登录</h2>
      <div class="input-group">
        <label for="username">用户名</label>
        <input type="text" v-model="username" id="username" placeholder="请输入用户名" />
      </div>
      <div class="input-group">
        <label for="password">密码</label>
        <input type="password" v-model="password" id="password" placeholder="请输入密码" />
      </div>
      <button class="login-button" @click="login">登录</button>
    </div>
  </template>

  <script>
  import { loginUser } from '../api/index';
  export default {
  name: 'LoginForm',
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
            this.$parent.isLoggedIn = true;
          } else {
            // 登录失败的处理，例如显示错误消息
          }
        })
       .catch((error) => {
          console.error('登录错误：', error);
        });
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.login-title {
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

.login-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>