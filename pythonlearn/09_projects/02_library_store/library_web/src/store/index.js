
import Vue from 'vue'
import Vuex from 'vuex'


// import storage from 'store'
Vue.use(Vuex);
import { loginUser } from '../api/index';

export default new Vuex.Store({
    state: {
      user:{},
      token:null,
    }, // 存放数据
    getters: {}, // 计算属性
    mutations: {
      SET_USERNAME(state, username) {
        state.user.username = username;
      },
      SET_TOKEN(state, token) {
        state.token = token;
      }

    }, // 修改state中数据的一些方法
    actions: {
      login({ commit }, {username, password}) {
        // 模拟登录请求
        return new Promise((resolve, reject) => {
          loginUser(username, password)
          .then((response) => {
              if (response.status) {
                // 登录成功后的处理，比如存储 token 并跳转到其他页面
                const result = response.data
                // storage.set('access_token', result.token)
                commit('SET_TOKEN', result.token)
                commit('SET_USERNAME', result.username)
                // commit('SET_USERID', result.id)
                // resolve(result.data);
              } else {
                // 登录失败的处理
                reject(new Error('登录失败'));
              }
            })
          .catch((error) => {
              // 处理错误情况
              console.error('登录错误：', error);
              reject(error)
            });
        });
    }, // 异步方法
    modules: {
      // user
    }
  }
})