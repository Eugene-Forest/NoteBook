===============================
使用文件
===============================

在写文档时，特别是写计算机类的文档，经常要使用外部文件的文本或代码。

在笔者学习 Sphinx 的过程中，主要以 ``literalinclude`` 指令引用代码文件，以 ``include`` 指令引用文本文件或其他特殊文件如 *.rst* 文件，以 ``image`` 或 ``figure`` 引用图片文件。

.. note:: 

   点击查看 ``literalinclude`` |代码块指令| 、 ``image`` |image指令| 以及 ``figure`` |figure指令| 指令的笔记。

.. _include-directive: 

include 指令
===============

.. include:: ../example/test.xml
   :code: xml

.. include:: ../example/Not_regular_expression.py
   :literal:
   :start-line: 0
   :end-line: 22
   :number-lines: 10

.. include:: ../example/title1.rst
   :start-line: 9
   :end-line: 16

.. raw:: html

   <hr width=300 size=10>

.. code-block:: rest
   :caption: 分界线以上的三个代码块的源码

   .. 上文代码如下：

   .. include:: ../example/test.xml
      :code: xml

   .. include:: ../example/Not_regular_expression.py
      :literal:
      :start-line: 0
      :end-line: 22
      :number-lines: 10

   .. include:: ../example/title1.rst
      :start-line: 9
      :end-line: 16


.. note:: 

   一般来说，可以通过 literalinclude-directive 来创建代码块，但是 include-directive 也可以完成相同的功能，区别在于后者没有前者的大多数选项。

.. attention:: 

   通过代码运行的结果可以知道，通过 include 指令时不附带 ``code`` 或 ``literal`` 选项，那么会向使用该命令的文件中导入目标文件中的内容并以 rest 语法被解析显示。


include-directive 有以下选项：

* ``start-line`` :  integer; 只包含从这一行开始的内容。(在Python中，通常第一行的索引是0，从末尾开始计数为负值。)
* ``end-line`` : integer; 直到(但不包括)这一行的内容。
* ``start-after`` : text to find in the external data file; 只包含指定文本第一次出现之后的内容。
* ``end-before`` : text to find in the external data file; 只包含指定文本第一次出现之前的内容。
* ``number-lines`` : [integer] (start line number);在每个代码行前面加上行号。可选参数是第一行的编号(默认为1)。
* ``literal`` : flag (empty);整个包含的文本作为单个文本块插入到文档中。
* ``code`` : [string] (formal language); 参数和包含的内容被传递给code指令(对于程序清单很有用)。
* ``parser`` : parser name;使用指定的解析器解析包含的内容。
* ``encoding`` : string; 外部数据文件的文本编码。默认为文档的input_encoding。
* ``tab-width`` : integer; 硬制表符扩展的空格数。负值可以防止硬标签的扩展。默认为tab_width配置设置。


.. raw:: html

   <hr width=600 size=10>

.. |代码块指令| replace:: :ref:`代码块指令<literalinclude-directive>` 
.. |image指令| replace:: :ref:`image指令<image-directive>` 
.. |figure指令| replace:: :ref:`figure指令<figure-directive>` 