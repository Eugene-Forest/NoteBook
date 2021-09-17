====================
基础杂糅知识
====================


字段列表
=================


example
---------------

:fieldname: Field content

:othername: othername field content

----

.. code-block:: rest

   :fieldname: Field content
   
   :othername: othername field content




文字块
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

----

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

topic / 主题 or 总论
==========================

.. topic:: Topic Title

   Subsequent indented lines comprise
   the body of the topic, and are
   interpreted as body elements.

.. code-block:: rest

   .. topic:: Topic Title

      Subsequent indented lines comprise
      the body of the topic, and are
      interpreted as body elements.


