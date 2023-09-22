# TypeScript

TypeScript 是 JavaScript 的一个超集，支持 ECMAScript 6 标准。

TypeScript 由微软开发的自由和开源的编程语言。

TypeScript 设计目标是开发大型应用，它可以编译成纯 JavaScript，编译出来的 JavaScript 可以运行在任何浏览器上。



* TypeScript 区分大写和小写字符。
* 分号是可选的 : 每行指令都是一段语句，你可以使用分号或不使用， 分号在 TypeScript 中是可选的，建议使用。


```{toctree}
:caption: TypeScript 语法集
:hidden:
:maxdepth: 2
:numbered:

数据类型 <data-type>
变量声明 <declare-variable>
流程处理 <flow-block>
字面量 <object-literal>
类型推导 <type-inference>
函数 <function>
类 <class-and-interface>
泛型 <generic>
关键字 <keyword>
封装对象 <package-object>
联合对象 <union-type>
命名空间 <namespace>
模块 <module>
声明文件 <declaration-file>
```


## 开始

在正式开始了解 TypeScript 语法之前，我们需要先部署好环境以及如何创建 TypeScript 下项目，在这里以基于 webpack 的 TypeScript 为示例。

在这里，我们默认环境中已经配置好 *node.js* 和 *npm* 环境。

在此练习中，你可以全局安装 *TypeScript* 。 在更大、更复杂的代码库中使用 *TypeScript* 时，建议切换到按项目安装，从而更好地控制项目的一致性。

```{admonition} 为什么使用 webpack

ES2015 中的 `import` 和 `export` 语句已经被标准化。但是大多数浏览器还无法支持它们，但是 `webpack` 却能够提供开箱即用般的支持。 

我们当然可以直接创建一个简单的 TypeScript 项目，但是在接触到模块的时候我们会发现，直接通过 `tsc` 命令产生的 Js 文件在浏览器中无法使用 `import` 和 `export` 语句。
```

### 安装 TypeScript

TypeScript 在 npm 注册表中以 typescript 包的形式提供。 安装最新版本的 TypeScript：

* 在“命令提示符”窗口中，输入 `npm install -g typescript`。
* 输入 `tsc` 确认已安装 TypeScript 。 如果已成功安装，则此命令应显示编译器命令和选项列表。


### 创建一个 TypeScript 项目

* 创建项目目录 `mkdir typescript-dome && cd typescript-dome`
* 进入文件夹，初始化 npm 环境 ： `npm init`
* npm 安装项目环境 typescript/tslint/ts-loader/webpack/webpack-cli : `npm install --save-dev typescript tslint webpack webpack-cli`
* 初始化 tslint 、 webpack : 
  * `./node_modules/.bin/tslint --init` 命令产生一个 *tslint.json* 文件




```{code-block} word
:caption: 项目结构构成（左边加号的文件意为手动添加）

  typescript-demo
  |- package.json (npm init 后产生的文件)
+ |- tsconfig.json (tsc --init 后产生的文件，使用模板即可)
  |- tslint.json (tslint --init 后产生的文件)
+ |- webpack.config.js
  |- /dist (webpack 构建后产生的文件)
    |- bundle.js
+   |- index.html （新建作为一个 demo 的初始文件）
  |- /src
+   |- index.ts
  |- /node_modules (npm install 后的包)
```



#### webpack.config.js 模板

这会直接将 webpack 的入口起点指定为 ./index.ts，然后通过 ts-loader _加载所有的 .ts 和 .tsx 文件，并且在当前目录输出_一个 bundle.js 文件。

```{code-block} js

const path = require('path');

module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ '.tsx', '.ts', '.js' ]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```


#### tsconfig.json 模板

这里我们设置一个基本的配置，来支持 JSX，并将 TypeScript 编译到 ES5……

```{code-block} json

{
  "compilerOptions": {
    "outDir": "./dist/",
    "noImplicitAny": true,
    "module": "es6",
    "target": "es5",
    "jsx": "react",
    "allowJs": true
  }
}
```
