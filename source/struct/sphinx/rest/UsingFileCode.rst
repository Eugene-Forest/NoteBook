========================
显示代码
========================

总得来说，codeblock代码块指令有两种形式，一种是直接将代码放入代码块中，另一种是引用已有的文件的代码将其放入代码块中。


代码形式：

* 前者： ``.. code-block:: code_language_type``
* 后者： ``.. literalinclude:: code_file_path(local or internet)``


.. seealso::
   
   `关于代码高亮 pygments 支持的语言 <https://pygments.org/languages/>`_ 

|75|

使用codeblock
===========================

.. code-block:: rest

   .. code-block:: java

      public class HelloWorld {
         public static void main(String[] args){
            System.out.println("Hello World!");
         }
      }

|15|

运行效果如下：

.. code-block:: java

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }

|50|

为代码块添加标题和 label 
============================


.. code-block:: java
   :caption: 代码块添加标题示例
   :name: HelloWorldExampleCodeBlock

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }

|15|

.. code-block:: rest
   :caption: 代码块添加标题示例代码

   .. code-block:: java
      :caption: 代码块添加标题
      :name: HelloWorldExampleCodeBlock

      public class HelloWorld {
         public static void main(String[] args){
            System.out.println("Hello World!");
         }
      }

|50|

显示行号
=========================

.. code-block:: rest

   .. code-block:: java
      :linenos:

      public class HelloWorld {
         public static void main(String[] args){
            System.out.println("Hello World!");
         }
      }

|15|
 
运行效果如下：

.. code-block:: java
   :linenos:

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }

|50|
 
突出特定行
========================

.. code-block:: rest

   .. code-block:: java
      :emphasize-lines: 1,3-5
      :linenos:

      public class HelloWorld {
         public static void main(String[] args){
            System.out.println("Hello World!");
         }
      }

|15|

突出3到5行的运行效果如下：

.. code-block:: java
   :emphasize-lines: 1,3-5
   :linenos:

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }

|50|

.. _literalinclude-directive:


引用一个文件 literalinclude
==================================

.. code-block:: rest

   .. literalinclude:: ../example/Not_regular_expression.py
      :language: python
      :linenos:
      :lines: 1-2,30-

|15|

运行结果如下；显示文件的第1到2行，以及30行之后的代码：

.. literalinclude:: ../example/Not_regular_expression.py
   :language: python
   :linenos:
   :lines: 1-2,30-

|50|

指定引用文件的方法，或类
================================

指令支持包含文件的一部分. 例如 Python模块, 可以选择类，函数或方法，使用 pyobject 选项。

.. code-block:: rest

   .. literalinclude:: ../example/Not_regular_expression.py
      :pyobject: isPhoneNumber

|15|

运行效果如下：

.. literalinclude:: ../example/Not_regular_expression.py
   :pyobject: isPhoneNumber

|50|


diff2个文件
===================

.. code-block:: rest

   .. literalinclude:: ../example/Not_regular_expression.py
      :diff: ../example/Not_regular_expression2.py

|15|

运行效果如下：

.. literalinclude:: ../example/Not_regular_expression.py
   :diff: ../example/Not_regular_expression2.py

|50|

锚点小测试
====================

点击前往 :ref:`代码块添加标题示例 <HelloWorldExampleCodeBlock>` 

|15|

.. code-block:: rest

   点击前往 :ref:`代码块添加标题示例 <HelloWorldExampleCodeBlock>` 
