# 计数信号量和semaphore类

## 引入

对于 single threaded execution mode , 是用于确保某个区域“只能由一个线程”执行。下面对这种模式进行扩展，用以确保某个区域“最多只能由N个线程”执行。这个时候就需要用信号量来控制线程数。

确保某个区域“最多只能由N个线程”执行的问题可转换为以下问题：

> 假设能够使用的资源只有N个，而需要使用这些资源的线程个数多于或远多于N个，这就会出现资源竞争，也就需要通过计数信号量进行资源管制。

java.util.concurrent包中提供了表示计数信号量的Semaphore类。

- 资源的许可个数（permits）将通过Semaphore类的构造函数来指定。
- Semaphore的acquire方法用于获取存在的可用资源。当存在资源是，执行该方法会减少一个可用资源并返回。若没有可用资源则会被阻塞在该语句中。
- Semaphore的release方法用于释放持有的资源。执行该方法后，信号量内部的资源会增加一个；另外，如果此时存在执行acquire方法正在等待的线程，那么其中一个线程会被唤醒并执行acquire返回。

## 示例

```{literalinclude} ../example_java/extend/Main.java
:emphasize-lines: 3,13,25,29,53
:language: java
```

运行结果：

```guess
Thread-6: BEGIN: used = 3
Thread-3: BEGIN: used = 3
Thread-4: BEGIN: used = 3
Thread-3: END:   used = 3
Thread-1: BEGIN: used = 3
Thread-1: END:   used = 3
Thread-7: BEGIN: used = 3
Thread-4: END:   used = 3
Thread-0: BEGIN: used = 3
Thread-7: END:   used = 3
Thread-8: BEGIN: used = 3
Thread-8: END:   used = 3
Thread-9: BEGIN: used = 3
Thread-6: END:   used = 3
Thread-5: BEGIN: used = 3
Thread-0: END:   used = 3
Thread-2: BEGIN: used = 3
Thread-5: END:   used = 3
Thread-2: END:   used = 2
Thread-3: BEGIN: used = 2
Thread-9: END:   used = 2
Thread-5: BEGIN: used = 2
Thread-1: BEGIN: used = 3
Thread-3: END:   used = 3
Thread-7: BEGIN: used = 3
Thread-5: END:   used = 3
Thread-1: END:   used = 2
Thread-7: END:   used = 1
Thread-9: BEGIN: used = 1
Thread-9: END:   used = 1
Thread-7: BEGIN: used = 1
Thread-7: END:   used = 1
Thread-0: BEGIN: used = 1
Thread-3: BEGIN: used = 2
Thread-3: END:   used = 2
Thread-7: BEGIN: used = 2
Thread-0: END:   used = 2
Thread-4: BEGIN: used = 2
Thread-2: BEGIN: used = 3
Thread-7: END:   used = 3
Thread-6: BEGIN: used = 3
Thread-4: END:   used = 3
Thread-6: END:   used = 2
Thread-1: BEGIN: used = 2
Thread-5: BEGIN: used = 3
Thread-2: END:   used = 3
Thread-8: BEGIN: used = 3
Thread-8: END:   used = 3
Thread-3: BEGIN: used = 3
Thread-5: END:   used = 3
Thread-2: BEGIN: used = 3
Thread-1: END:   used = 3
Thread-7: BEGIN: used = 3
Thread-3: END:   used = 3
Thread-5: BEGIN: used = 3
Thread-7: END:   used = 2
Thread-6: BEGIN: used = 3
Thread-2: END:   used = 3
Thread-2: BEGIN: used = 3
Thread-5: END:   used = 3
Thread-2: END:   used = 2
Thread-9: BEGIN: used = 2
Thread-6: END:   used = 2
Thread-0: BEGIN: used = 2
Thread-8: BEGIN: used = 3
Thread-8: END:   used = 3
Thread-9: END:   used = 2
//Ctrl+C结束
```

由结果可看出，十个线程在相互争夺资源，但是最多有三个线程持有资源。
