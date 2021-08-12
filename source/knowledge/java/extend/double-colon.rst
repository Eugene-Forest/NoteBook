=======================
双冒号的用法
=======================


JDK 8 中有双冒号的用法，就是把方法当做参数传到 stream 内部，使 stream 的每个元素都传入到该方法里面执行一下。

关于 Stream 的相关笔记 :ref:`点击前往<java-stream>` 

示例1
---------

.. literalinclude:: ../example_java/extend/stream/DoubleColon.java
   :language: Java
   :linenos:


.. code-block:: word

   输出一和输出二均为：
   
   eugene
   forest
   jackson

示例2
-----------

.. literalinclude:: ../example_java/extend/stream/DStream.java
   :language: Java
   :linenos:


输出结果不确定，但是其结果一定是10个整数随机数。

