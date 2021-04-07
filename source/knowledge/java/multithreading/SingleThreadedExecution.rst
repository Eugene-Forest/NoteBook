===============================================
single threaded execution mode (one by one)
===============================================

.. note:: 

   关键词： ``synchronized`` 

.. tip:: 

   当前线程是否已获取某一对象的锁可以通过Thread.holdsLock()来确认。当前线程已获取对象的锁时，可使用assert来表示：

   .. code-block:: java

      //若持有锁，那么不会报错
      assert Thread.holdsLock(obj);

synchronized关键字的使用
=========================

**只要是访问 多个线程共享的字段 的方法，就需要使用synchronized进行保护。**


每个示例拥有一个独立的锁。因此，并不是说某一个实例中的 synchronized 方法正在执行，其他实例的 synchronized 方法就不能运行了。

线程要执行 synchronized的实例方法，就必须要获取this的锁，而能获取一个实例的锁的线程只能有一个，正是因为这种唯一性，才能够使用 synchronized来实现 Single Threaded Execution mode。

实例不同，对应的锁就不一样。但是对于代码块 ``synchronized (Something.class) {...}`` 以及被synchronized修饰的静态方法，它对Something这个类的所有实例有同步作用。

.. code-block:: java

   public class TestThread extends Thread{
      
      synchronized void PrintMessage() {
         for(int i=1;i<100;i++) {
            System.out.print(i+" ");
            if (i%10==0) {
               System.out.println("");
            }
            else if (i==99) {
               System.out.println("");
            }
         }
      }
      
      static synchronized void HoldIt() {
         for(int i=1;i<100;i++) {
            System.out.print(i+" ");
            if (i%10==0) {
               System.out.println("");
            }
            else if (i==99) {
               System.out.println("");
            }
         }
      }
      
      void HoldThem() {
         synchronized (TestThread.class) {
            for(int i=1;i<100;i++) {
               System.out.print(i+" ");
               if (i%10==0) {
                  System.out.println("");
               }
               else if (i==99) {
                  System.out.println("");
               }
            }
         }
      }
      
      @Override
      public void run() {
         PrintMessage(); //result 1
   //		HoldIt(); //result 2
      }
   }

   public class TestMain {
	
	public static void main(String[] args) {
		Thread userThread=new TestThread();
		Thread staticThread=new TestThread();
		userThread.start();
		staticThread.start();
	   }
   }


.. code-block:: word

   //result 1
   1 2 3 4 1 2 3 5 6 4 5 6 7 8 9 10 7 
   11 8 9 10 
   12 13 11 12 13 14 15 16 17 14 18 19 20 
   15 16 17 18 21 22 19 20 
   23 24 25 26 21 22 23 27 28 29 30 
   31 32 33 34 35 36 24 25 26 27 28 29 30 
   31 32 33 34 35 36 37 38 39 40 
   41 42 43 44 45 46 47 48 49 50 
   51 37 38 39 40 
   41 42 43 44 52 53 45 46 47 48 49 54 50 
   51 52 53 54 55 56 57 55 58 59 60 
   61 56 57 58 62 59 60 
   63 64 65 66 67 68 69 70 
   71 72 73 74 75 76 77 78 79 80 
   81 82 83 84 85 86 87 88 89 90 
   91 61 62 63 92 93 94 95 96 97 98 99 
   64 65 66 67 68 69 70 
   71 72 73 74 75 76 77 78 79 80 
   81 82 83 84 85 86 87 88 89 90 
   91 92 93 94 95 96 97 98 99 

.. code-block:: word

   //result 2
   1 2 3 4 5 6 7 8 9 10 
   11 12 13 14 15 16 17 18 19 20 
   21 22 23 24 25 26 27 28 29 30 
   31 32 33 34 35 36 37 38 39 40 
   41 42 43 44 45 46 47 48 49 50 
   51 52 53 54 55 56 57 58 59 60 
   61 62 63 64 65 66 67 68 69 70 
   71 72 73 74 75 76 77 78 79 80 
   81 82 83 84 85 86 87 88 89 90 
   91 92 93 94 95 96 97 98 99 
   1 2 3 4 5 6 7 8 9 10 
   11 12 13 14 15 16 17 18 19 20 
   21 22 23 24 25 26 27 28 29 30 
   31 32 33 34 35 36 37 38 39 40 
   41 42 43 44 45 46 47 48 49 50 
   51 52 53 54 55 56 57 58 59 60 
   61 62 63 64 65 66 67 68 69 70 
   71 72 73 74 75 76 77 78 79 80 
   81 82 83 84 85 86 87 88 89 90 
   91 92 93 94 95 96 97 98 99 


.. note:: 

   synchronized静态方法是使用该类的类对象的锁来执行线程的互斥处理，TestThread.class是TestThread类对应的java.lang.Class类的实例。
