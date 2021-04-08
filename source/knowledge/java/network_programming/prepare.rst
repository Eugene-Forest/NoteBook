================================
知识准备
================================


java 多线程
-----------------

------------
线程池
------------




java socket
------------------


ServerSocket的isClosed()方法判断ServerSocket是否关闭，只有执行了ServerSocket的close()方法，isClosed()方法才返回true；否则，即使ServerSocket还没有和特定端口绑定，isClosed()方法也会返回false。

ServerSocket的isBound()方法判断ServerSocket是否已经与一个端口绑定，只要ServerSocket已经与一个端口绑定，即使它已经被关闭，isBound()方法也会返回true。

如果需要确定一个ServerSocket已经与特定端口绑定，并且还没有被关闭，则可以采用以下方式：

.. code-block:: java

   boolean isOpen=serverSocket.isBound() && !serverSocket.isClosed();

