const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: (config) => {
    if (process.env.NODE_ENV !== 'production') {
      config.devtool = 'source-map'
    }
  },
  devServer: {
    client: {
      overlay: false // 编译错误时，取消全屏覆盖（建议关掉）
    }
  }
})
