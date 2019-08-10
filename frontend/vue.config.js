module.exports = {
    outputDir: "../server/dist",
    // relative to outputDir
    assetsDir: "static",
    // update below to URL of project
    publicPath: 'http://localhost:5000/',

    devServer: {
      proxy: {
        '/api*': {
          // Forward frontend dev server request for /api to flask dev server
          target: 'http://localhost:5000/'
        }
      }
    }

};
