import { createStore } from 'vuex';


export default createStore({
    state: {
      username:localStorage.getItem('username') || null,
      token:localStorage.getItem('token') || null,
      logined:localStorage.getItem('logined') || null,
    }, // 存放数据
    getters: {
      isLoggedIn: (state) => !!state.token,
      getUserName: (state) => state.username,
    }, // 计算属性
    mutations: {
      SET_USERNAME(state, username) {
        state.username = username;
        localStorage.setItem('username', username); 
      },
      SET_TOKEN(state, token) {
        state.token = token;
        localStorage.setItem('token', token); 
      },
      SET_LOGINED(state, logined) {
        state.logined = logined;
        localStorage.setItem('logined', logined); 
      },
      CLEAR_STATUS(state) {
        state.token = null;
        state.username = null;
        state.logined = false;
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        localStorage.removeItem('logined');
      },

    }, // 修改state中数据的一些方法
    actions: {
      // 异步保存用户信息
      login({ commit }, { username, token }) {
        console.log(username)
        console.log(token)
        // 可以添加实际的登录 API 请求逻辑
        commit('SET_USERNAME', username);
        commit('SET_TOKEN', token);
        commit('SET_LOGINED', true);
      },
      // 异步登出
      logout({ commit }) {
        // 可以添加实际的登出 API 请求逻辑
        commit('CLEAR_STATUS');
      },
    }, // 异步方
    modules: {
      // user
    }
})