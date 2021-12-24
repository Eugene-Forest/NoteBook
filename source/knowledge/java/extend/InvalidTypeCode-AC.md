# StreamCorruptedException: invalid type code: AC

在使用 socket 设计网络通信程序时，笔者分别为发送数据和接受数据的操作以线程形式运行。代码如下：

**发送数据的线程关键代码如下：**

```java
public void run() {
    try {
        //没有判断套接字是否关闭，可能会出错
        ObjectOutputStream oos=new ObjectOutputStream(new BufferedOutputStream(socket.getOutputStream()));
        oos.writeObject(messageModel);
        oos.flush();
    } catch (Exception e) {
       e.printStackTrace();
    }
}
```

**接受数据的线程关键代码如下：**

```java
public void run() {
    try {
        MessageModel messageModel;
        while (true) {
             //每次接受一次信息都要更新读取对象，显然不太合适
            in = new ObjectInputStream(new BufferedInputStream(socket.getInputStream()));
            messageModel = (MessageModel)in.readObject();
        }
    } catch (Exception e) {

    }
}
```

笔者的预期是，当两个聊天端建立连接后，接收数据的线程将一直运行等待并接收数据，而发送数据的线程将只会发送一次数据。这种设计看似没有问题，但是接收线程实际上只能正确得接收一次数据，当第二次接收数据时会出现 `AC` 错误。

因为输出对象流在将对象序列化的时候会在第一次加一个head上去，后面继续传输的时候省去了这一个步骤。而相对应的接受这个对象的输入流在第一次的时候去掉这个头，此后直接读取。因此，只要有任意一方多次封装了对象流（或者多次通过 socket 的 io 流 new 一个对象流），就会造成重复加head或者重复去head，导致错误。
