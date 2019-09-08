const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/App.jsx', //  Точка входа
    output:{
        path:path.resolve(__dirname, ''), // Абсолютный путь
        filename: 'static/frontend/bundle.js' // Этот файл будет создан
    },
    resolve: {
        extensions: ['.', '.js', '.jsx'],
    },
    mode: 'development', // Режим сборки
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/, // Принимать правила к ...
                exclude: /node_modules/, // За исключением ...
                use: 'babel-loader' // Применять эти правила
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: ['css-loader']
                })
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({filename: 'static/frontend/style.css'}),
        new HtmlWebpackPlugin({
            inject: false,
            template: './src/index.html',
            filename: 'templates/frontend/index.html'
        })
    ],
    devServer: {
        port: 8080,
        historyApiFallback:true,
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
            "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
        }
    }
};
