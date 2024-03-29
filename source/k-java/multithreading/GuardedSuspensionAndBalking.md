# Guarded suspension mode and Balking mode

Guarded suspension mode [^id6] 以及 Balking mode [^id7] 都是是类似于 “附加条件的 synchronized” 这样的模式。

这两者在条件达成的情况下的执行情况与一般的 single threaded execution mode一样;
但是当条件不能满足其继续运行下去时，前者则暂停（执行wait）并等待条件达成（执行notifyAll），
后者则直接中断方法的运行。

## Guarded suspension mode 实例(等待我准备好)

| 类名         | 说明           |
| ------------ | -------------- |
| Request      | 表示一个请求类 |
| RequestQueue | 存放请求的类   |
| ClientThread | 发送请求的类   |
| ServerThread | 接收请求的类   |
| Main         | 测试类         |

### Request

该类是 immutable 类，是线程安全的。

```{literalinclude} ../example_java/multithreading/GuardedSuspension/Request.java
:language: java
```

### RequestQueue

LinkedList对象是非线程安全的。对于wait的唤醒条件notify/notifyAll放置的位置需要考量。

```{literalinclude} ../example_java/multithreading/GuardedSuspension/RequestQueue.java
:emphasize-lines: 9,11,16,21,22
:language: java
:linenos: true
```

### ClientThread

```{literalinclude} ../example_java/multithreading/GuardedSuspension/ClientThread.java
:language: java
```

### ServerThread

```{literalinclude} ../example_java/multithreading/GuardedSuspension/ServerThread.java
:language: java
```

### Main类

```{literalinclude} ../example_java/multithreading/GuardedSuspension/Main.java
:language: java
```

### 运行(例子)

通过运行可知，无论服务线程和客户线程的开启先后，其第一个打印的线程必定为客户线程。

```guess
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
```

:::{tip}
使用 Guarded suspension 模式需要注意程序的生存性。考虑到这种模式的实现通过 wait 以及 notifyAll 来实现，需要意识到会有执行了 wait 但是却没执行 notifyAll,以及执行了 notifyAll 但是从来没有执行 wait 的极端情况。
:::

## Balking mode 实例(不需要就算了)

| 类名          | 说明                   |
| ------------- | ---------------------- |
| Data          | 可修改并保存的数据的类 |
| SaverThread   | 定期保存数据的类       |
| ChangerThread | 修改并保存数据内容的类 |
| Main          | 测试类                 |

### Data

```{literalinclude} ../example_java/multithreading/Balking/Data.java
:language: java
```

### ChangerThread

```{literalinclude} ../example_java/multithreading/Balking/ChangerThread.java
:language: java
```

### SaverThread

```{literalinclude} ../example_java/multithreading/Balking/SaverThread.java
:language: java
```

### Main

```{literalinclude} ../example_java/multithreading/Balking/Main.java
:language: java
```

### 运行（实例）

```guess
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
```

:::{tip}
可使用 Balking 模式的情况————实现闭锁。所谓闭锁，一般针对“状态仅变化一次的变量”,如下Something类中的 initialized 变量一样，一般针对的是初始化以及终止处理这类“不会执行两次及以上的处理”。

```{literalinclude} ../example_java/multithreading/Balking/Something.java
:language: java
```
:::

## time out模式

通过以上两种模式的例子可知，其实际执行的语句都是比较极端的，比如 Guarded suspension模式中如果条件永远不满足那么就可能永远地等待下去；而 Balking 模式中如果条件不满足就立马停止操作在实际使用中可能也会受到限制。那么作为这两者地折中方案，Guarded timed 模式就可以极好地解决。

% //todo 添加time out模式笔记
 
[^id6]: Guarded suspension : 防护着的暂停

[^id7]: Balking : 阻停
