# 安装并初始化原始项目

项目后端采用的是 BladeX 的简单版本 BladeX Boot, 该版本的文件可以在 [BladeX 的开源仓库](https://gitee.com/smallc/SpringBlade/tree/boot/)  中 boot 分支中获取，而前端的文件可以直接克隆  [官网 Saber 仓库](https://gitee.com/smallc/Saber)  即可。

## BladeX Boot

- 克隆 [BladeX 的开源仓库](https://gitee.com/smallc/SpringBlade/tree/boot/)  中 boot 分支
- 切换到 boot 分支
- 创建并初始化 mysql 数据库，名字自定义即可，使用项目文件下的两个 sql 文件： `/doc/sql/blade-saber-mysql.sql` 和 `/doc/sql/blade-update-3.1.0~3.2.0.sql`
- 将 dev 配置文件中的数据库和用户密码改为自己的
- 重新初始化项目仓库

:::{figure} ../../img/project/bladex/boot/dev-sql.png
:alt: dev-sql

dev 配置文件修改和获取sql文件
:::

:::{sidebar} 开发手册
[开发手册网盘链接](https://pan.baidu.com/s/1j8sQPBlUt9CWROvzqSOnrQ) 提取码：1244

```{image} ./file/bladex_doc.png
:alt: "\u5F00\u53D1\u624B\u518C"
:scale: 30%
```
:::



## Saber

- 克隆  [官网 Saber 仓库](https://gitee.com/smallc/Saber)
- 参考开发手册
- 配置源
- 安装项目依赖
- 重新初始化项目仓库

### 安装和配置源

以下命令前提为安装了 `nodejs` 和 `npm` 。

```guess
Microsoft Windows [版本 10.0.19043.1348]
(c) Microsoft Corporation。保留所有权利。

C:\Users\qaz22> npm install -g yarn --registry=https://registry.npm.taobao.org

> yarn@1.22.17 preinstall C:\Program Files\nodejs\node_global\node_modules\yarn
> :; (node ./preinstall.js > /dev/null 2>&1 || true)

C:\Program Files\nodejs\node_global\yarn -> C:\Program Files\nodejs\node_global\node_modules\yarn\bin\yarn.js
C:\Program Files\nodejs\node_global\yarnpkg -> C:\Program Files\nodejs\node_global\node_modules\yarn\bin\yarn.js
+ yarn@1.22.17
added 1 package in 0.868s

C:\Users\qaz22> yarn config set registry https://registry.npm.taobao.org -g
yarn config v1.22.17
success Set "registry" to "https://registry.npm.taobao.org".
Done in 0.09s.
```

### 安装项目依赖

```bash
Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-WorkCatalog/bladex-saber (master)
$ yarn install
yarn install v1.22.17
info No lockfile found.
[1/4] Resolving packages...
......
[2/4] Fetching packages...
warning url-loader@1.1.2: Invalid bin field for "url-loader".
[3/4] Linking dependencies...
warning " > sass-loader@7.3.1" has unmet peer dependency "webpack@^3.0.0 || ^4.0.0".
[4/4] Building fresh packages...
success Saved lockfile.
Done in 93.93s.
```

## 重新初始化项目仓库

成功运行了项目后（除了接口文档的功能无法使用），我们需要将项目的本地仓库重置，方法十分简单：

- 将项目根目录下的 `.git` 和 `.idea` 文件夹（Idea 和 WebStorm 的项目配置信息文件夹 `.idea` ）删除
- 然后通过 Idea 和 WebStorm 重新打开项目，然后在项目文件根目录下重新初始化仓库( `git init` )即可。
