========================
表格指令 table-directive
========================


Grid Table 在多数情况下都比较难以使用，而且只有在借助额外插件的情况下才能较为快速地生成。

reST 除了 Grid Table 的无标题表格使用 , 还有 table、csv_table、list_table 指令。

.. _table-directive:

table(directive)
======================

带有标题的一般表格和不带有标题的一般表格

=====  =====
  A    not A
=====  =====
False  True
True   False
=====  =====


.. table:: Truth table for "not"
   :widths: 1,2
   :align: center
   :width: 50%

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====



.. code-block::  rest

   .. 代码如下 
   
   =====  =====
    A    not A
   =====  =====
   False  True
   True   False
   =====  =====


   .. table:: Truth table for "not"
      :widths: 1,2
      :align: center
      :width: 50%

      =====  =====
       A    not A
      =====  =====
      False  True
      True   False
      =====  =====

.. note:: 
   所谓带有标题的表格只是在以往的简单表格结构上添加指令，同样的道理，Grid Table 也可以添加 table 指令来携带标题或进行其他调整。


table 指令有以下属性：

* ``align`` : "left", "center", or "right" ； 用来调整表格在页面中的水平位置。
* ``widths`` : "auto", "grid", or *a list of integers* (如果对于一个有两列n行的表格，那么它的属性值可为 **1,2**) ； 用来调整表格的每个列的占比。
* ``width`` : 长度或百分比 ； 用来调整表格的宽度。

.. _csv-table:

csv-table
===================


.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


.. csv-table:: 使用本地csv文件
   :file: ../example/csv_table_example.csv 

.. csv-table:: 将前行csv数据作为 header
   :file: ../example/csv_table_example.csv
   :header-rows: 2
   
.. csv-table:: 将前两列csv数据作为 header
   :file: ../example/csv_table_example.csv
   :stub-columns: 2
   
.. csv-table:: 需要双倍使用分隔符才能将分隔符显示
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30
   :stub-columns: 1

   "Gannet Ripple", 1.99, "He said, ""On a stick!"" "

.. csv-table:: 使用 · 来 替代引号作为分隔符
   :header: Treat, Quantity, Description
   :widths: 15, 10, 30
   :quote: ·

   ·Albatross·, 2.99, ·On a stick!·
   ·Crunchy Frog·, 1.49, ·If we took the bones out, it wouldn't be
   crunchy, now would it?·
   ·Gannet Ripple·, 1.99, ·he said,"On a stick!"·

----

代码如下：

.. code-block:: rest

   .. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
      crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"


   .. csv-table:: 使用本地csv文件
      :file: ../example/csv_table_example.csv 

   .. csv-table:: 将前2行csv数据作为 header
      :file: ../example/csv_table_example.csv
      :header-rows: 2
      
   .. csv-table:: 将前两列csv数据作为 header
      :file: ../example/csv_table_example.csv
      :stub-columns: 2
      
   .. csv-table:: 需要双倍使用分隔符才能将分隔符显示
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30
      :stub-columns: 1

      "Gannet Ripple", 1.99, "He said, ""On a stick!"" "

   .. csv-table:: 使用 · 来 替代引号作为分隔符
      :header: Treat, Quantity, Description
      :widths: 15, 10, 30
      :quote: ·

      ·Albatross·, 2.99, ·On a stick!·
      ·Crunchy Frog·, 1.49, ·If we took the bones out, it wouldn't be
      crunchy, now would it?·
      ·Gannet Ripple·, 1.99, ·he said,"On a stick!"·


csv-table 指令有以下属性：

* ``align`` : "left", "center", or "right" ； 用来调整表格在页面中的水平位置。
* ``widths`` : "auto", "grid", or *a list of integers* (如果对于一个有两列n行的表格，那么它的属性值可为 **1,2**) ； 用来调整表格的每个列的占比。
* ``width`` : 长度或百分比 ； 用来调整表格的宽度。
* ``file`` : The local filesystem path to a CSV data file.
* ``url`` :  An Internet URL reference to a CSV data file.
* ``encoding`` : string ； 外部CSV数据(文件或URL)的文本编码。默认为文档的编码(如果指定)。
* ``header-rows`` : 要在表头中使用的CSV数据行数。默认值为0。
* ``stub-columns`` : 要在表头中使用的CSV数据列数。默认值为0。
* ``header`` : 表头的补充数据，独立于主CSV数据的任何 ``header-rows`` (标题行)并在其之前添加。必须使用与主CSV数据相同的CSV格式。
* ``delim`` : 用于分隔字段的 **单字符字符串**。默认为 ``,``(逗号)。 空格为 ``space`` ，tab 为 ``tab`` 。
* ``quote`` : 一个单字符字符串，用于引用包含分隔符的元素或以引号字符开头的元素。默认为 ``"`` (quote/引号)
* ``keepspace`` : flag (empty);将紧跟在分隔符后面的空格视为有意义的。默认是忽略这些空白。


.. important:: 

   * 在csv-table的字符串有需要使用双引号或单引号，同时分隔符quote为 ``"``，只需要双倍使用即可，如数据为 **"He said, ""Hi!"""**

.. _list-table:

list-table
========================


一个统一的两级项目符号列表。

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

代码如下：

.. code-block:: rest

   .. list-table:: Frozen Delights!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
        - Quantity
        - Description
      * - Albatross
        - 2.99
        - On a stick!
      * - Crunchy Frog
        - 1.49
        - If we took the bones out, it wouldn't be
         crunchy, now would it?
      * - Gannet Ripple
        - 1.99
        - On a stick!


list-table 指令有以下属性：

* ``align`` : "left", "center", or "right" ； 用来调整表格在页面中的水平位置。
* ``widths`` : "auto", "grid", or *a list of integers* (如果对于一个有两列n行的表格，那么它的属性值可为 **1,2**) ； 用来调整表格的每个列的占比。
* ``width`` : 长度或百分比 ； 用来调整表格的宽度。
* ``header-rows`` : 要在表头中使用的数据行数。默认值为0。
* ``stub-columns`` : 要在表头中使用的数据列数。默认值为0。