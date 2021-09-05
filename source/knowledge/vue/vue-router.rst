===================
vue-router
===================

Vue-router 是给 Vue.js 提供路由管理的插件，利用 hash 的变化控制动态组件的切换。以往页面间跳转都由后端 MVC 中的 Controller 层控制，通过 <a> 标签的 href 或者直接修改 location.href，我们会向服务端发起一个请求，服务端响应后根据所接收到的信息去获取数据和指派对应的模板，渲染成 HTML 再返回给浏览器，解析成我们可见的页面。Vue.js + Vue-router 的组合将这一套逻辑放在了前端去执行，切换到对应的组件后再向后端请求数据，填充进模板来，在浏览器端完成 HTML 的渲染。这样也有助于前后端分离，前端不用依赖于后端的逻辑，只需要后端提供数据接口即可。


.. note:: 

   :ref:`点击前往路由笔记 <vue-router-prepare>` 。
   
   官方 vue-router 文档 `点击前往 <https://router.vuejs.org/zh/>`_   