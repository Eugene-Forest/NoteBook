=========================
域
=========================

最初，sphinx是为一个项目而设计的，即Python语言的文档。不久之后，它作为一个文档工具被提供给了每个人，但是Python模块的文档仍然是深入内置的——最基本的指令，比如 function ，是为Python对象设计的。由于Sphinx已经变得有点受欢迎，所以在使用它时有很多不同的兴趣：C/C++项目、JavaScript、甚至RealStReWorkType标记（如本文中的文档）。

域是标记（RestructuredText）的集合 directive 和 role ）描述并链接到 object 属于一起的，例如编程语言的元素。域中的指令名和角色名的名称如下 domain:name ，例如 py:function . 域还可以提供自定义索引（如python模块索引）。

.. attention:: 

   简单来说，域是用来编写接口（API）文档的。 [#]_


例如：

.. function:: pyfunc()

   Describes a Python function.

.. js:function:: $.getJSON(href, callback[, errback])

   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.

.. raw:: html

   <hr width=400 size=10>

.. code-block:: rest

   .. function:: pyfunc()

      Describes a Python function.

   .. js:function:: $.getJSON(href, callback[, errback])

      :param string href: An URI to the location of the resource.
      :param callback: Gets called with the object.
      :param errback:
         Gets called in case the request fails. And a lot of other
         text so we need multiple lines.
      :throws SomeError: For whatever reason in that case.
      :returns: Something.


----


.. [#] 2021年9月28日：待以后需要使用相关知识时在进行学习笔记。官网：https://www.osgeo.cn/sphinx/usage/restructuredtext/domains.html#role-math-numref 