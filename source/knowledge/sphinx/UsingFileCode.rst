========================
显示代码
========================



使用codeblock
===========================

.. code-block:: word

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

.. code-block:: word

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

.. code-block:: word

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

.. code-block:: word

   .. literalinclude:: ../../conf.py
      :language: python
      :linenos:
      :lines: 1-3,5,220-

运行结果如下；显示配置文件的第1到3行，第5行，以及220行之后的代码：

.. literalinclude:: ../../conf.py
   :language: python
   :linenos:
   :lines: 1-3,5,220-


指定引用文件的方法，或类
================================

指令支持包含文件的一部分. 例如 Python模块, 可以选择类，函数或方法，使用 pyobject 选项。

.. code-block:: word

   .. literalinclude:: ./example/Not_regular_expression.py
      :pyobject: isPhoneNumber

运行效果如下：

.. literalinclude:: ./example/Not_regular_expression.py
   :pyobject: isPhoneNumber




diff2个文件
===================

.. code-block:: word

   .. literalinclude:: ./example/Not_regular_expression.py
      :diff: ./example/Not_regular_expression2.py


运行效果如下：

.. literalinclude:: ./example/Not_regular_expression.py
   :diff: ./example/Not_regular_expression2.py
