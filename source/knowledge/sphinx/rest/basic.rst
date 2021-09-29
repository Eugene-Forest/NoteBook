====================
基础杂糅知识
====================


字段列表
=================

通常在文章的名词解释中使用。

example
---------------

:fieldname: Field content

:othername: othername field content

.. raw:: html

   <hr width=400 size=10>

.. code-block:: rest

   :fieldname: Field content
   
   :othername: othername field content




文字块 ``::``
======================

文字代码块 (ref）以特殊标记结束段落 :: . 文本块必须缩进（和所有段落一样，用空行与周围段落分隔）：：

处理 :: 标记很智能：

* 如果它是以自己的段落出现的，则该段落完全不在文档中。
* 如果前面有空白，则删除标记。
* 如果前面有非空白，则标记将被单个冒号替换。


example
------------

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

.. raw:: html

   <hr width=400 size=10>

上文的语法格式如下：

.. code-block:: rest

   This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.


注释
=====================

.. 这是注释

.. 
   这是注释

.. code-block:: rest

   .. 这是注释

   .. 
      这是注释


脚注/尾注
===============

使用 ``[#name]_`` 标记脚注位置，并将脚注正文添加到文档底部的“footnotes”标题后面，

.. code-block:: rest

   自动脚注 : 脚注参考 [#]_ ，这是第二个脚注 [#]_ 。

   脚注参考 [5]_

   .. raw:: html

      <hr width=400 size=10>

   ..  [#] 这是第一个注记的信息
   ..  [#] 这是第二个注记的信息
   ..  [5] 这是对应的注记信息

.. note:: 
   运行效果如下方所示。

.. raw:: html

   <hr width=400 size=10>


自动脚注 : 脚注参考 [#]_ ，这是第二个脚注 [#]_ 。

脚注参考 [5]_

.. raw:: html

   <hr width=400 size=10>

..  [#] 这是第一个注记的信息
..  [#] 这是第二个注记的信息
..  [5] 这是对应的注记信息


索引
============

超链接
-----------
.. code-block:: rest

   `Title <http://link>`_ 

.. raw:: html

   <hr width=400 size=10>

文档内部链接（锚）
-------------------

在这里，只介绍其中一种方法。

.. code-block:: rest

   //在目标位置添加标签
   .. _label-name:

.. code-block:: rest

   //在起始位置添加指向链接
   :ref:`link title <label-name>` 


