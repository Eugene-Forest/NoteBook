===============================
使用文件
===============================

在写文档时，特别是写计算机类的文档，经常要使用外部文件的文本或代码。

在笔者学习 Sphinx 的过程中，主要以 ``literalinclude`` 指令引用代码文件，以 ``include`` 指令引用文本文件或其他特殊文件如 .rst 文件，以 ``image`` 或 ``figure`` 引用图片文件。

.. note:: 

   点击查看 ``literalinclude`` |代码块指令| 、 ``image`` |image指令| 以及 ``figure`` |figure指令| 指令的笔记。


include 指令
===============

.. include:: ../example/csv_table_example.csv
   :end-line: 3
   :literal:
   :number-lines: 

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

   .. 上文代码如下：

   .. include:: ../example/csv_table_example.csv
      :end-line: 3
      :literal:
      :number-lines: 

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

include-directive 有以下选项：

* ``start-line`` :  integer;
* ``end-line`` : integer;
* ``start-after`` : integer;
* ``end-before`` : integer;
* ``number-lines`` : [integer] (start line number);
* ``literal`` : flag (empty);
* ``code`` : [string] (formal language);
* ``parser`` : parser name;
* ``encoding`` : string;
* ``tab-width`` : integer;


.. raw:: html

   <hr width=600 size=10>

.. |代码块指令| replace:: :ref:`代码块指令<literalinclude-directive>` 
.. |image指令| replace:: :ref:`image指令<image-directive>` 
.. |figure指令| replace:: :ref:`figure指令<figure-directive>` 