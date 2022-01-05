# GitHub登录/访问难问题

## 修改DNS

:::{warning}
以下添加的DNS服务器是阿里公共DNS服务器。然而以笔者现阶段使用情况（登录github）而言，效果并不理想，推荐与方法2同时用。
:::

打开网络和共享中心

```{image} ../img/network-share.png
:alt: network share
```

点击左侧功能 *更改适配器设置* ,前往网络连接面板。

```{image} ../img/internet-connect.png
:alt: internet connect
```

右键属性进入：

```{image} ../img/DNS.png
:alt: DNS
```

点击网络属性的网络协议版本4，并通过下方属性按钮进入网络协议版本4属性编辑，具体如上图。

## 修改hosts文件

在系统中找到 hosts 文件

Window：C:\\Windows\\System32\\drivers\\etc\\hosts （或 Linux：/etc/hosts）

向hosts文件放入一下两个 IP 地址的代码，代码如下：

```guess
# GitHub Start
140.82.114.4 github.com
199.232.69.194 github.global.ssl.fastly.net
# GitHub End
```

保存退出。

在 CMD 命令行中执行 `ipconfig/flushdns`

```guess
C:\>ipconfig/flushdns

Windows IP 配置

已成功刷新 DNS 解析缓存。
```

:::{note}

通过修改hosts文件的效果目前 [^id2] 良好。使用个人移动网络的效果会更好。
:::

[^id2]: 2021年3月19日 测试
