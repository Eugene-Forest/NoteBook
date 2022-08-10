# NPM install

我们在使用 `npm install` 安装模块的模块的时候 ，一般会使用下面这几种命令形式：

```{code-block} bash

npm install moduleName # 安装模块到项目目录下
 
npm install -g moduleName # -g 的意思是将模块安装到全局，具体安装到磁盘哪个位置，要看 npm config prefix 的位置。
 
npm install -save moduleName # -save 的意思是将模块安装到项目目录下，并在package文件的dependencies节点写入依赖。
 
npm install -save-dev moduleName # -save-dev 的意思是将模块安装到项目目录下，并在package文件的devDependencies节点写入依赖。
```


* `npm install moduleName` 命令

    1. 安装模块到项目 *node_modules* 目录下。
    2. 不会将模块依赖写入 *devDependencies* 或 *dependencies* 节点。
    3. 运行 `npm install` 初始化项目时不会下载模块。

* `npm install -g moduleName` 命令

    1. 安装模块到全局，不会在项目 *node_modules* 目录中保存模块包。
    2. 不会将模块依赖写入 *devDependencies* 或 *dependencies* 节点。
    3. 运行 `npm install` 初始化项目时不会下载模块。

* `npm install -save moduleName` 命令

    1. 安装模块到项目 *node_modules* 目录下。
    2. 会将模块依赖写入 *dependencies* 节点。
    3. 运行` npm install` 初始化项目时，会将模块下载到项目目录下。
    4. 运行 `npm install --production` 或者注明 *NODE_ENV* 变量值为 *production* 时，会自动下载模块到 *node_modules* 目录中。

* `npm install -save-dev moduleName` 命令

    1. 安装模块到项目 *node_modules* 目录下。
    2. 会将模块依赖写入 *devDependencies* 节点。
    3. 运行 `npm install` 初始化项目时，会将模块下载到项目目录下。
    4. 运行 `npm install --production` 或者注明 *NODE_ENV* 变量值为 *production* 时，不会自动下载模块到 *node_modules* 目录中。


*devDependencies* 节点下的模块是我们在开发时需要用的，比如项目中使用的 gulp ，压缩css、js的模块。这些模块在我们的项目部署后是不需要的，所以我们可以使用 `-save-dev` 的形式安装。像 express 这些模块是项目运行必备的，应该安装在 *dependencies* 节点下，所以我们应该使用 `-save` 的形式安装。



