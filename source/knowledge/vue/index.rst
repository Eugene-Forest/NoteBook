======================
vue 以及 element-ui
======================


.. note:: 
   记录在学习vue以及element-ui过程中的心得以及知识点。

vue
=============

* 官方编辑器 `HBuilder <https://www.dcloud.io/>`_ 
* 官方学习文档 `vue 2.x教程 <https://cn.vuejs.org/v2/guide/>`_
* 官方API `vue 2.x API <https://cn.vuejs.org/v2/api/>`_ 
* 官方cookbook `cookbook <https://cn.vuejs.org/v2/cookbook/>`_ 

---------------------
通过网络引入——CDN引入
---------------------

对于制作原型或学习，你可以这样使用最新版本：

.. code-block:: html

   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

对于生产环境，我们推荐链接到一个明确的版本号和构建文件，以避免新版本造成的不可预期的破坏：

.. code-block:: html

   <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>

--------------
下载本地包
--------------

直接下载并用 <script> 标签引入，Vue 会被注册为一个全局变量。

最新的文件请到官网下载。 `>>点击前往官网>> <https://cn.vuejs.org/v2/guide/installation.html>`_ 

.. toctree::
   :caption: vue目录
   :numbered:
   :maxdepth: 2

   起步 <start>
   指令 <instruction>


element-ui
=================

---------
CDN引入
---------

.. code-block:: html

   <!-- 引入样式 -->
      <link rel="stylesheet" href="https://unpkg.com/element-ui@2.15.1/lib/theme-chalk/index.css">
   <!-- import Vue before Element -->
   ...
   <!-- 引入组件库 -->
   <script src="https://unpkg.com/element-ui@2.15.1/lib/index.js"></script>


这段代码表示引入的element-ui版本为2.15.1，该版本是笔者记录时的最新版本。将版本固定有利于项目的稳定性。

虽然通过链接引入样式以及js十分简单，但是从网络传输的角度上来说比较费时。比较好的方法时在服务器本机上添加element-ui支持。

-------------------
通过vue-cli导入
-------------------

#. 下载对应本机环境安装 node.js 默认NPM已经集成。`node.js 官网下载 <https://nodejs.org/zh-cn/>`_ 。打开 cmd 直接输入测试是否安装成功; node测试 ``node -v`` ; NPM 测试 ``npm -v``。
#. 安装淘宝镜像 ``npm install -g cnpm --registry=https://registry.npm.taobao.org``。
#. 安装vue ``cnpm install vue -g``。
#. 安装 vue-cli ``cnpm install vue-cli -g``。
#. 安装 element-ui ``cnpm install -g element-ui -S``。
#. 安装webpack ``cnpm install -g webpack``。


.. code-block:: cmd

   # clone the project
   git clone https://github.com/PanJiaChen/vue-element-admin.git

   # enter the project directory
   cd vue-element-admin

   # install dependency
   npm install

   # develop
   npm run dev

.. toctree::
   :caption: element-ui 目录
   :numbered:
   :maxdepth:2

   起步 <element-ui/start>


