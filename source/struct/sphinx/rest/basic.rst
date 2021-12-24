====================
基础杂糅知识
====================


字段列表
=================

通常在文章的名词解释中使用。

字段列表 example
-----------------------

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


文字块 example
----------------------

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


.. _Python-a: http://www.python.org

:ref:`python <Python-a>` 

* ```Title <http://link>`_`` 
* ``.. _Python: http://www.python.org``

.. code-block:: rest

   `Title <http://link>`_ 

.. raw:: html

   <hr width=400 size=10>

文档内部链接（锚）
-------------------

在这里，只介绍其中一种方法,那就就是直接添加到标题前。

.. code-block:: rest

   //在目标位置添加标签
   .. _label-name:

.. code-block:: rest

   //在起始位置添加指向链接
   :ref:`link title <label-name>` 

|50|

列表
===================

单级符号列表
-------------------

列表的使用比较简单，而且可使用的符号也有多种选择：

* This is a bulleted list.
* It has two items, the second item uses two lines.

- This is a bulleted list.
- It has two items, the second item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

5) This is a numbered list.
6) It has two items too.


.. code-block:: rest
   :caption: 单级符号列表的源码

   * This is a bulleted list.
   * It has two items, the second item uses two lines.

   - This is a bulleted list.
   - It has two items, the second item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

   1) This is a numbered list.
   2) It has two items too.

|30|

两级符号列表 [#]_
-------------------

也可以嵌套列表，但注意它们必须通过空行与父列表项分开:

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues
* This is a bulleted list.

  * This is a bulleted list.
  * It has two items, the second item uses two lines.

* 第一级列表第一句

  * 这是两级列表第一句
  * 两级列表第二句


.. code-block:: rest
   :caption: 嵌套列表的源码表示

   * this is
   * a list

      * with a nested list
      * and some subitems

   * and here the parent list continues
   * This is a bulleted list.

      * This is a bulleted list.
      * It has two items, the second item uses two lines.

   * 第一级列表第一句

      * 这是两级列表第一句
      * 两级列表第二句

|30|

定义列表
---------------------


请注意，一个术语可以有很多段，段与段之间用空行分隔，但一段只能有一行文本。

引用的段落只是通过缩进它们来创建，而不是根据周围的段落创建。

定义列表 term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

定义列表 next term
   Description.

.. code-block:: rest
   :caption: 定义列表

   定义列表 term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   定义列表 next term
      Description.

|30|

定义列表与两级符号列表的使用
------------------------------

我们通过比较定义列表与符号列表可以发现，在两级列表的表示情况下，显然是定义列表的显示比较友好，因为其一级列表有字体加重；而如果两级符号列表想要达到类似的效果则需要手动添加字体加重。
而将两者混合使用即可：

* 定义列表 term (up to a line of text)
   * Definition of the term, which must be indented
   * and can even consist of multiple paragraphs

* 定义列表 next term
   * Description.

.. code-block:: rest
   :caption: 定义列表与两级符号列表混合使用

   * 定义列表 term (up to a line of text)
      * Definition of the term, which must be indented
      * and can even consist of multiple paragraphs

   * 定义列表 next term
      * Description.

.. warning:: 

   带有数字标号的列表在与定义列表混合时会出现问题。

|30|



field lists
------------------------

字段列表与定义列表相似。

:Hello: This field has a short field name, so aligning the field
        body with the first line is feasible.

:Number-of-African-swallows-required-to-carry-a-coconut: It would
    be very difficult to align the field body with the left edge
    of the first line.  It may even be preferable not to begin the
    body on the same line as the marker.
   

.. code-block:: rest
   :caption: field lists 示例源码

   :Hello: This field has a short field name, so aligning the field
         body with the first line is feasible.

   :Number-of-African-swallows-required-to-carry-a-coconut: It would
      be very difficult to align the field body with the left edge
      of the first line.  It may even be preferable not to begin the
      body on the same line as the marker.
   



----


.. [#] 一般来说，两级列表足以应付多数情况，而且也不推荐使用两级以上的列表。