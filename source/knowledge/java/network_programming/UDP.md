# UDP

与socket套接字不同的是，客户端与服务器之间不需要连接，一方可以随时向另一方以报文DatagramPacket的方式发送信息，至于消息是否按顺序到达，或者对方是否正确接收，它都不关心。

## 创建DatagramSocket

DatagramSocket 有多个构造方法

`DatagramSocket()`：创建一个DatagramSocket实例，并将该对象绑定到本机默认IP地址、本机所有可用端口中随机选择的某个端口。

`DatagramSocket(int prot)`：创建一个DatagramSocket实例，并将该对象绑定到本机默认IP地址、指定端口。

`DatagramSocket(int port, InetAddress laddr)`：创建一个DatagramSocket实例，并将该对象绑定到指定IP地址、指定端口。

通过上面三个构造器中的任意一个构造器即可创建一个DatagramSocket实例。

## DatagramSocket的connect和bind方法

`void connect(SocketAddress addr)` :将此套接字连接到远程套接字地址（IP地址+端口号）。

`bind(SocketAddress addr)` :将此DatagramSocket绑定到特定的地址和端口。

:::{note}
两个方法的意思是将socket与指定地址绑定，绑定成功后只能往该地址发送数据。并不是建立连接，因为udp是面向非连接的
:::

## 简单实例

```java
DatagramSocket mSocket = new DatagramSocket();
//需要发送的数据
byte[]datas = "data"
//hostIP 需要发送的地址
InetAddress address = InetAddress.getByName(hostIP);
//需要发送的数据包，hostPort 发送的端口
DatagramPacket packet = new DatagramPacket(datas, datas.length, address, hostPort);
//发送数据
mSocket.send(packet);
```

```java
DatagramSocket mSocket = new DatagramSocket();
//持续接收数据
while(!mSocket){
   byte datas[] = new byte[256];
   DatagramPacket packet = new DatagramPacket(datas, datas.length);
   mSocket.receive(packet);//阻塞调用，直到返回数据
   String receiveMsg = new String(packet);
}
```

:::{note}
使用DatagramSocket发送数据报时，DatagramSocket并不知道将该数据报发送到哪里，而是由DatagramPacket自身决定数据报的目的地。在该例子中接收数据时，DatagramPacket并没有指定地址，默认所有地址的包都能接收。
:::
