var webpack = require('webpack');
module.exports = {
  entry: [
    "./js/app.js"
  ],
  output: {
    path: __dirname + '/static',
    publicPath: '/',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
      }
    ]

  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  plugins: [
  ]
};
