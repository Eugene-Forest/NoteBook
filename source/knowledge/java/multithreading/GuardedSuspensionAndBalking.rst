============================================
Guarded suspension mode and Balking mode
============================================


Guarded suspension mode [#]_ 以及 Balking mode [#]_ 都是是类似于 “附加条件的 synchronized” 这样的模式。

这两者在条件达成的情况下的执行情况与一般的 single threaded execution mode一样;
但是当条件不能满足其继续运行下去时，前者则暂停（执行wait）并等待条件达成（执行notifyAll），
后者则直接中断线程运行。


Guarded suspension mode 实例(等待我准备好)
============================================


+--------------+----------------+
|     类名     |      说明      |
+==============+================+
| Request      | 表示一个请求类 |
+--------------+----------------+
| RequestQueue | 存放请求的类   |
+--------------+----------------+
| ClientThread | 发送请求的类   |
+--------------+----------------+
| ServerThread | 接收请求的类   |
+--------------+----------------+
| Main         | 测试类         |
+--------------+----------------+

Request
---------

该类是 immutable 类，是线程安全的。

.. literalinclude:: ../example_java/multithreading/GuardedSuspension/Request.java
   :language: java

RequestQueue
---------------

LinkedList对象是非线程安全的。对于wait的唤醒条件notify/notifyAll放置的位置需要考量。

.. literalinclude:: ../example_java/multithreading/GuardedSuspension/RequestQueue.java
   :language: java
   :linenos:
   :emphasize-lines: 9,11,16,21,22

ClientThread
---------------

.. literalinclude:: ../example_java/multithreading/GuardedSuspension/ClientThread.java
   :language: java

ServerThread
-------------------

.. literalinclude:: ../example_java/multithreading/GuardedSuspension/ServerThread.java
   :language: java

Main
-------

.. literalinclude:: ../example_java/multithreading/GuardedSuspension/Main.java
   :language: java

运行(例子)
-----------

通过运行可知，无论服务线程和客户线程的开启先后，其第一个打印的线程必定为客户线程。

.. code-block:: word

   Alice requests [ Request No.0 ]
   Bobby handles  [ Request No.0 ]
   Alice requests [ Request No.1 ]
   Alice requests [ Request No.2 ]
   Bobby handles  [ Request No.1 ]
   Bobby handles  [ Request No.2 ]
   Alice requests [ Request No.3 ]
   Bobby handles  [ Request No.3 ]
   Alice requests [ Request No.4 ]
   Bobby handles  [ Request No.4 ]
   Alice requests [ Request No.5 ]
   Alice requests [ Request No.6 ]
   Bobby handles  [ Request No.5 ]
   Bobby handles  [ Request No.6 ]
   Alice requests [ Request No.7 ]
   Bobby handles  [ Request No.7 ]
   Alice requests [ Request No.8 ]
   Bobby handles  [ Request No.8 ]


Balking mode 实例(不需要就算了)
==================================

+---------------+------------------------+
|     类名      |          说明          |
+===============+========================+
| Data          | 可修改并保存的数据的类 |
+---------------+------------------------+
| SaverThread   | 定期保存数据的类       |
+---------------+------------------------+
| ChangerThread | 修改并保存数据内容的类 |
+---------------+------------------------+
| Main          | 测试类                 |
+---------------+------------------------+


Data
------------

.. literalinclude:: ../example_java/multithreading/Balking/Data.java
   :language: java


ChangerThread
-----------------

.. literalinclude:: ../example_java/multithreading/Balking/ChangerThread.java
   :language: java

SaverThread
---------------

.. literalinclude:: ../example_java/multithreading/Balking/SaverThread.java
   :language: java

Main
-------

.. literalinclude:: ../example_java/multithreading/Balking/Main.java
   :language: java

运行（实例）
===========

.. code-block:: word

   SaverThread calls doSave, content = No.0
   SaverThread calls doSave, content = No.1
   ChangerThread calls doSave, content = No.2
   SaverThread calls doSave, content = No.3
   ChangerThread calls doSave, content = No.4
   SaverThread calls doSave, content = No.5
   SaverThread calls doSave, content = No.6
   ChangerThread calls doSave, content = No.7
   SaverThread calls doSave, content = No.8
   ChangerThread calls doSave, content = No.9
   ChangerThread calls doSave, content = No.10
   ChangerThread calls doSave, content = No.11
   SaverThread calls doSave, content = No.12
   ChangerThread calls doSave, content = No.13
   ChangerThread calls doSave, content = No.14
   SaverThread calls doSave, content = No.15

----

.. [#] Guarded suspension : 防护着的暂停
.. [#] Balking : 阻停