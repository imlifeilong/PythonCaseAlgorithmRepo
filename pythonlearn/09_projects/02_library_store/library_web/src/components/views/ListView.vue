<template>
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
  </template>
  
  <script>
  export default {
    name: "ListView",
    data() {
      return {
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
    },
  };
  </script>
  
  <style scoped>
  .book-list {
    padding: 20px 0;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .book-items {
    display: grid;
    grid-template-columns: repeat(5, 1fr); /* 每行显示3本书 */
    gap: 20px;
  }
  
  .book-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 10px;
    /* border: 1px solid #eaeaea; */
    border-radius: 10px;
    background-color: #fff;
    transition: box-shadow 0.3s ease;
  }
  
  .book-item:hover {
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .book-item img {
    width: 120px;
    height: 180px;
    object-fit: cover;
    margin-bottom: 10px;
    border-radius: 5px;
  }
  
  .book-title {
    font-size: 16px;
    font-weight: bold;
    margin: 10px 0 5px;
  }
  
  .book-author {
    font-size: 14px;
    color: #666;
  }
  
  /* 分页组件样式 */
  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin-top: 20px;
  }
  
  .pagination button {
    padding: 5px 10px;
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
  </style>
  