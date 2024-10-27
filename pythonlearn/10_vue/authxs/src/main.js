import { createApp } from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';	// Element 1
import 'element-ui/lib/theme-chalk/index.css'; // Element 2

// 关闭 Vue 的生产提示
Vue.config.productionTip = false

// 使用插件
Vue.use(ElementUI); // Element 3

// 创建 Vue 实例对象
new Vue({
  render: h => h(App),
}).$mount('#app')