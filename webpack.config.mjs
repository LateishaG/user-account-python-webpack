import path from 'path';
const __dirname = new URL('.', import.meta.url).pathname;

export default {
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/')
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        resolve: {
          fullySpecified: false
        },
        options: {
          presets: ['@babel/preset-react']
        }
      }
    ]
  }
};
