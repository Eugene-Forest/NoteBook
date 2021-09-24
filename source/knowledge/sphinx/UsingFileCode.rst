========================
显示代码
========================

总得来说，codeblock代码块指令有两种形式，一种是直接将代码放入代码块中，另一种是引用已有的文件的代码将其放入代码块中。


代码形式：

* 前者： ``.. code-block:: code_language_type``
* 后者： ``.. code-block:: code_file_path(local or internet)``




使用codeblock
===========================

.. code-block:: rest

   .. code-block:: java

      public class HelloWorld {
         public static void main(String[] args){
            System.out.println("Hello World!");
         }
      }

运行效果如下：

.. code-block:: java

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }


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

 
运行效果如下：

.. code-block:: java
   :linenos:

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }


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


突出3到5行的运行效果如下：

.. code-block:: java
   :emphasize-lines: 1,3-5
   :linenos:

   public class HelloWorld {
      public static void main(String[] args){
         System.out.println("Hello World!");
      }
   }


引用一个文件
==================================

.. code-block:: rest

   .. literalinclude:: ./example/Not_regular_expression.py
      :language: python
      :linenos:
      :lines: 1-2,30-

运行结果如下；显示文件的第1到2行，以及30行之后的代码：

.. literalinclude:: ./example/Not_regular_expression.py
   :language: python
   :linenos:
   :lines: 1-2,30-


指定引用文件的方法，或类
================================

指令支持包含文件的一部分. 例如 Python模块, 可以选择类，函数或方法，使用 pyobject 选项。

.. code-block:: rest

   .. literalinclude:: ./example/Not_regular_expression.py
      :pyobject: isPhoneNumber

运行效果如下：

.. literalinclude:: ./example/Not_regular_expression.py
   :pyobject: isPhoneNumber




diff2个文件
===================

.. code-block:: rest

   .. literalinclude:: ./example/Not_regular_expression.py
      :diff: ./example/Not_regular_expression2.py


运行效果如下：

.. literalinclude:: ./example/Not_regular_expression.py
   :diff: ./example/Not_regular_expression2.py
