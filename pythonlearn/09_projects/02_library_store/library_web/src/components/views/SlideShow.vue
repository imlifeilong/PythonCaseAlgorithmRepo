<template>
  <div>
  <header class="page-header">
  <div class="container">
    <!-- Logo -->
    <div class="logo">MyWebsite</div>

    <!-- Navigation Menu -->
    <nav class="nav-menu">
      <a href="#" class="nav-item">Home</a>
      <a href="#" class="nav-item">About</a>
      <a href="#" class="nav-item">Services</a>
      <a href="#" class="nav-item">Contact</a>
    </nav>

    <!-- Search Bar -->
    <div class="search-bar">
      <template v-if="isLoggedIn">
        <!-- 显示下拉菜单 -->
        <div class="user-menu">
          <button class="user-btn" @click="toggleDropdown">{{ username }}</button>
          <ul v-show="showDropdown" class="dropdown-menu">
            <li><a href="/mybooks">我的书籍</a></li>
            <li><a href="/profile">个人信息</a></li>
            <li><a href="/logout" @click="logout">退出</a></li>
          </ul>
        </div>
      </template>
      <template v-else>
        <!-- 显示登录按钮 -->
        <button class="search-btn" type="button" @click="goToLogin">登录</button>
      </template>
    </div>
  </div>
</header>
  <!-- <CarouselView /> -->
  <ListView />
</div>
</template>

<script>

// import CarouselView from './CarouselView.vue';
import ListView from './ListView.vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    // const router = useRouter();

    const username = store.getters.getUserName || '未知用户';
    const isLoggedIn = store.getters.isLoggedIn || false;

    console.log(username)
    console.log(isLoggedIn)
    
    // const logout = () => {
    //   store.dispatch('logout');
    //   router.push('/login');
    // };

    return {
      username,
      isLoggedIn,
      // logout,
    };
  },
  name: "SlideShow",
  components: {
    // CarouselView,
    ListView
  },
  data() {
  return {
    // isLoggedIn: false, // 用户登录状态
    showDropdown: false, // 下拉菜单是否显示
    // username: '', // 用户名
  };
},
methods: {
    // 模拟获取登录状态
    checkLoginStatus() {
      // 假设从后端 API 获取用户信息
      // 示例数据：假设用户登录返回 { isLoggedIn: true, username: 'JohnDoe' }
      // axios.get('/api/auth/status').then((response) => {
      //   this.isLoggedIn = response.data.isLoggedIn;
      //   this.username = response.data.username;
      // });
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    goToLogin() {
      // 跳转到登录页面
      window.location.href = '/login';
    },
    logout() {
      // 调用注销 API，然后刷新页面或更新状态
      // axios.post('/api/auth/logout').then(() => {
      //   this.isLoggedIn = false;
      //   this.username = '';
      //   this.showDropdown = false;
      //   alert('您已成功退出登录！');
      // });
    },
  },
  mounted() {
    this.checkLoginStatus(); // 检查用户登录状态
  },
};
</script>

<style scoped>
/* Base Styles */
.page-header {
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 15px 0;
  position: sticky;
  top: 0;
  z-index: 1000;
}

/* Container */
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Logo */
.logo {
  font-size: 24px;
  font-weight: bold;
  color: #007bff;
}

/* Navigation Menu */
.nav-menu {
  display: flex;
  gap: 20px;
}

.nav-item {
  text-decoration: none;
  color: #333;
  font-size: 16px;
  transition: color 0.3s;
}

.nav-item:hover {
  color: #007bff;
}

/* Search Bar */
.search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-input {
  width: 200px;
  padding: 8px 10px;
  border: 1px solid #ddd;
  border-radius: 20px;
  font-size: 14px;
  transition: box-shadow 0.3s;
}

.search-input:focus {
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
  outline: none;
}

.search-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 15px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.search-btn:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .menu-icon {
    display: block;
  }

  .nav-menu {
    flex-direction: column;
    position: absolute;
    top: 60px;
    right: 20px;
    background-color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    overflow: hidden;
    transform: translateY(-150%);
    width: 200px;
    padding: 10px;
  }

  .nav-menu.is-open {
    transform: translateY(0);
  }
}

</style>
