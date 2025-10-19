<template>
  <div>
    <div class="carousel">
      <!-- Carousel Content -->
      <div class="slides" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
        <div class="slide" v-for="(image, index) in images" :key="index">
          <img :src="image" alt="Carousel Image" />
        </div>
      </div>
  
      <!-- Navigation Dots -->
      <div class="dots">
        <span
          v-for="(image, index) in images"
          :key="index"
          :class="{ active: currentIndex === index }"
          @click="goToSlide(index)"
        ></span>
      </div>
    </div>
    <div class="category-nav">
    <ul class="category-list">
      <li 
        v-for="(category, index) in categories" 
        :key="index" 
        :class="{ active: activeCategory === category }" 
        @click="selectCategory(category)">
        {{ category }}
      </li>
    </ul>
  </div>
  <!-- <div class="book-list">
    <div class="book-item" v-for="(book, index) in books" :key="index">
      <img :src="book.cover" alt="Book Cover" class="book-cover" />
      <div class="book-details">
        <h3 class="book-title">{{ book.title }}</h3>
        <p class="book-author">作者：{{ book.author }}</p>
        <p class="book-category">分类：{{ book.category }}</p>
        <p class="book-description">{{ book.description }}</p>
      </div>
    </div>

    <div class="pagination">
      <button :disabled="currentPage === 1" @click="prevPage">上一页</button>
      <span>第 {{ currentPage }} 页 / 共 {{ totalPages }} 页</span>
      <button :disabled="currentPage === totalPages" @click="nextPage">下一页</button>
    </div>
  </div> -->
  <div class="book-list">
      <!-- 图书列表 -->
      <div class="book-items">
        <div class="book-item" v-for="(book, index) in paginatedBooks" :key="index">
          <img :src="book.cover" alt="Book Cover" />
          <h3 class="book-title">{{ book.title }}</h3>
          <p class="book-author">{{ book.author }}</p>
        </div>
      </div>
  
      <!-- 分页组件 -->
      <div class="pagination">
        <button :disabled="currentPage === 1" @click="prevPage">上一页</button>
        <span>第 {{ currentPage }} 页 / 共 {{ totalPages }} 页</span>
        <button :disabled="currentPage === totalPages" @click="nextPage">下一页</button>
      </div>
    </div>
</div>
  </template>
  
  <script>


  export default {
    name: "CarouselView",
    data() {
      return {
        images: [
          "https://via.placeholder.com/1200x400/007bff/ffffff?text=Slide+1",
          "https://via.placeholder.com/1200x400/6c757d/ffffff?text=Slide+2",
          "https://via.placeholder.com/1200x400/28a745/ffffff?text=Slide+3",
        ],
        categories: [
        "全部",
        "畅销书",
        "文学",
        "推理",
        "科幻",
        "历史",
        "旅行",
        "美食",
        "教育",
        "心理",
        "艺术",
        "经典",
        "社会",
        "成长",
        "美食",
        "教育",
        "心理",
        "艺术",
        "经典",
        "社会",
        "成长",
      ],
      books: [
      { title: "图书1", description: "探索美食的奥秘。", category: "美食",author: "作者1", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书2", description: "探索美食的奥秘。", category: "美食",author: "作者2", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书3", description: "探索美食的奥秘。", category: "美食",author: "作者3", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书4", description: "探索美食的奥秘。", category: "美食",author: "作者4", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书5", description: "探索美食的奥秘。", category: "美食",author: "作者5", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书6", description: "探索美食的奥秘。", category: "美食",author: "作者6", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书7", description: "探索美食的奥秘。", category: "美食",author: "作者7", cover: "https://pic.arkread.com/cover/ebook/f/451846511.1703837771.jpg!cover_default.jpg" },
        { title: "图书8", description: "探索美食的奥秘。", category: "美食",author: "作者8", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书9", description: "探索美食的奥秘。", category: "美食",author: "作者9", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书10", description: "探索美食的奥秘。", category: "美食",author: "作者10", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书11", description: "探索美食的奥秘。", category: "美食",author: "作者11", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书11", description: "探索美食的奥秘。", category: "美食",author: "作者11", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书11", description: "探索美食的奥秘。", category: "美食",author: "作者11", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书11", description: "探索美食的奥秘。", category: "美食",author: "作者11", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "图书11", description: "探索美食的奥秘。", category: "美食",author: "作者11", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },
        { title: "Python编程：从入门到实践", description: "探索美食的奥秘。", category: "美食",author: "[美] 埃里克·马瑟斯", cover: "https://pic.arkread.com/cover/ebook/f/122163837.1653694565.jpg!cover_default.jpg" },

      ],
      currentPage: 1,
        itemsPerPage: 15, // 每页显示的图书数量
      // currentPage: 1,
      // itemsPerPage: 10, // 每页显示的图书数量
      // activeCategory: "全部", // 当前选中的分类
      //   currentIndex: 0,
      //   intervalId: null,
      };
    },
    computed: {
      
    totalPages() {
      return Math.ceil(this.books.length / this.itemsPerPage);
    },
    paginatedBooks() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.books.slice(startIndex, endIndex);
    },
  },
    mounted() {
      this.startAutoSlide();
      
    },
    beforeUnmount() {
      this.stopAutoSlide();
    },
    methods: {
      prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
      selectCategory(category) {
      this.activeCategory = category;
      // 在此触发分类点击事件，例如：通过 emit 通知父组件加载相应内容
      this.$emit("categorySelected", category);
      },
      startAutoSlide() {
        this.intervalId = setInterval(() => {
          this.nextSlide();
        }, 3000);
      },
      stopAutoSlide() {
        clearInterval(this.intervalId);
      },
      nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
      },
      goToSlide(index) {
        this.currentIndex = index;
      },
    },
  };
  </script>
  
  <style scoped>
.book-list {
  padding: 20px 0;
  max-width: 1000px;
  margin: 0 auto;
  /* margin-left: 0px; */
}

.book-item {
  /* display: flex; */
  /* gap: 20px; */
  /* align-items: flex-start; */
  /* padding: 15px; */
  /* margin-bottom: 20px; */
  /* border: 0px solid #eaeaea; */
  /* border-radius: 2px; */
  /* background-color: #fff; */
  /* box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05); */
  /* transition: transform 0.3s ease, box-shadow 0.3s ease; */
    display: grid;
    grid-template-columns: repeat(5, 1fr); /* 每行显示3本书 */
    gap: 20px;
}

.book-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.book-cover {
  width: 120px;
  height: 180px;
  object-fit: cover;
  border-radius: 2px;
}

.book-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.book-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.book-author,
.book-category,
.book-description {
  font-size: 14px;
  color: #666;
  margin: 5px 0;
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  margin-top: 20px;
}

.pagination button {
  padding: 8px 15px;
  font-size: 14px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination span {
  font-size: 14px;
  color: #333;
}

.category-nav {
  /* background-color: #f9f9f9; */
  padding: 30px 0px; /* 增加内边距以靠左 */
  border-bottom: 1px solid #eaeaea;
  width: 100%;
  max-width: 1200px; /* 与轮播图宽度一致 */
  margin: 0 auto; /* 居中显示 */
  box-sizing: border-box;
}

.category-list {
  display: flex;
  flex-wrap: wrap; /* 换行显示 */
  gap: 15px; /* 分类之间的间距 */
  padding: 0;
  margin: 0;
  list-style: none;
}

.category-list li {
  padding: 8px 15px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 6px;
  background-color: #f4f4f4;
}

.category-list li:hover {
  background-color: #e6f0ff;
  color: #007bff;
}

.category-list li.active {
  background-color: #007bff;
  color: #fff;
}

  .carousel {
    position: relative;
    width: 100%;
    max-width: 1200px;
    margin: 20px auto;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  
  .slides {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .slide {
    min-width: 100%;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f4f4f4;
  }
  
  .slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
  }
  
  /* Navigation Dots */
  .dots {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
  }
  
  .dots span {
    width: 12px;
    height: 12px;
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
  }
  
  .dots span.active {
    background-color: #007bff;
    transform: scale(1.2);
  }
  </style>
  