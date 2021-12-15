============
起步
============

* 官方编辑器 `HBuilder <https://www.dcloud.io/>`_ 
* 官方学习文档 `vue 2.x教程 <https://cn.vuejs.org/v2/guide/>`_
* 官方API `vue 2.x API <https://cn.vuejs.org/v2/api/>`_ 
* 官方cookbook `cookbook <https://cn.vuejs.org/v2/cookbook/>`_ 


通过网络引入——CDN引入
---------------------

对于制作原型或学习，你可以这样使用最新版本：

.. code-block:: html

   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

对于生产环境，我们推荐链接到一个明确的版本号和构建文件，以避免新版本造成的不可预期的破坏：

.. code-block:: html

   <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>


下载本地包
--------------

直接下载并用 <script> 标签引入，Vue 会被注册为一个全局变量。

最新的文件请到官网下载。 `>>点击前往官网>> <https://cn.vuejs.org/v2/guide/installation.html>`_ 


Vue Devtools
-------------

在使用 Vue 时，我们推荐在你的浏览器上安装 Vue Devtools。它允许你在一个更友好的界面中审查和调试 Vue 应用。

快速且简单的安装Vue Devtools的方法：

* 通过使用火狐浏览器的官方插件商店里获取并安装插件。缺点是只能在火狐浏览器中使用该调试工具,而且刚刚安装后此插件的激活有些慢（安装后通过火狐浏览器打开vue文件以激活在开发者工具中的Vue工具窗口）。


.. //todo : vue 入门篇/引入篇