# 多线程设计模式

参考书籍：图解Java多线程设计模式 \[结城浩\]
 
一个Java Application运行后，在系统中是作为一个进程。

对于一般情况下启动的用户线程，是不会随主线程(main函数)的终止而终止的。

只有在所有的线程终止之后，程序才会终止。需要注意的是，**Java程序的终止是除守护线程(Daemon Thread)以外的线程的全部终止**。

守护线程是执行后台作业的线程，通过ThreadObject.setDaemon()来将用户线程设置为守护线程，需要注意的是，要在线程对象执行start前设置才有用。
 
```{toctree}
:caption: catalog
:maxdepth: 2
:numbered: true

single threaded execution mode <SingleThreadedExecution>
Guarded suspension mode and Balking mode <GuardedSuspensionAndBalking>
```
