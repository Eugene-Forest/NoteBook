# Nacos

```{important}

* 快速开始旨在帮助您快速上手安装、部署及入门使用Nacos，本快速开始所生产出的Nacos服务为单机模式及未开启鉴权，建议仅在测试中使用，若在实际生产环境中部署，请部署集群模式并开启鉴权，以避免存在稳定性和安全性的风险。
* **Nacos定义为一个IDC内部应用组件，并非面向公网环境的产品，建议在内部隔离网络环境中部署，强烈不建议部署在公共网络环境**
```

## 准备

* Nacos Server 的软件包下载： [Nacos Server 官网](https://nacos.io/download/nacos-server/)
* Nacos Server 的运行环境需要 JDK >= 1.8。
  * JDK 软件包 下载： [Java 1.8](https://www.oracle.com/java/technologies/downloads/#java8); 需要注意，要安装 ***64 位版本的 JDK***, Nacos 会出现启动错误。

## Window 下配置 Nacos

### 快速开始（单机模式 + 未开启鉴权）

快速开始的情况下，Nacos 的运行十分简单，不需要更改任何配置文件，直接将 Nacos 软件包解压后，在 `nacos\bin` 路径下，我们可以看到 以下两个文件：

1. `startup.cmd`
2. `shutdown.cmd`

从名字就可以知道分别是开启和关闭服务的文件。

* 启动命令(standalone代表着单机模式运行，非集群模式): `startup.cmd -m standalone`
* 关闭命令，双击 `shutdown.cmd` 即可，或者如果是窗口命令行启动，那么直接 `Ctl + C` 也可以结束服务。

* 打开控制台页面： `http://127.0.0.1:8848/nacos`

### 单机模式 + 开启鉴权

按照官方文档配置启动,默认是不需要登录的，这样会导致配置中心对外直接暴露。而启用鉴权之后，需要在使用用户名和密码登录之后，才能正常使用nacos。

* 开启鉴权之前，application.properties中的配置信息为：

```properties

### If turn on auth system:
nacos.core.auth.enabled=false
```

* 开启鉴权之后，application.properties中的配置信息为：

```properties

### If turn on auth system:
nacos.core.auth.system.type=nacos
nacos.core.auth.enabled=true
```

#### 自定义密钥

开启鉴权之后，你可以自定义用于生成JWT令牌的密钥，application.properties中的配置信息为：

```properties

### The default token(Base64 String):
nacos.core.auth.default.token.secret.key=SecretKey012345678901234567890123456789012345678901234567890123456789

### 2.1.0 版本后
nacos.core.auth.plugin.nacos.token.secret.key=SecretKey012345678901234567890123456789012345678901234567890123456789
```

```{important}

* 文档中提供的密钥为公开密钥，在实际部署时请更换为其他密钥内容，防止密钥泄漏导致安全风险。
* 在2.2.0.1版本后，社区发布版本将移除以文档如下值作为默认值，需要自行填充，否则无法启动节点。
* 密钥需要保持节点间一致，长时间不一致可能导致403 invalid token错误。
```

* 自定义密钥时，推荐将配置项设置为Base64编码的字符串，且原始密钥长度不得低于32字符。例如下面的的例子：

```properties

### The default token(Base64 String):
nacos.core.auth.default.token.secret.key=VGhpc0lzTXlDdXN0b21TZWNyZXRLZXkwMTIzNDU2Nzg=

### 2.1.0 版本后
nacos.core.auth.plugin.nacos.token.secret.key=VGhpc0lzTXlDdXN0b21TZWNyZXRLZXkwMTIzNDU2Nzg=
```

鉴权开关是修改之后立马生效的，不需要重启服务端。动态修改token.secret.key时，请确保token是有效的，如果修改成无效值，会导致后续无法登录，请求访问异常。

````{tip}

如何生成自定义密匙，可以通过下方 Java 代码实现：

```java

/**
 * <p>
 * nacos中JWT令牌密钥生成器<br>
 * 生成 nacos.core.auth.plugin.nacos.token.secret.key 的值
 * </p>
 */
public class NacosSecretUtil {
    public static void main(String[] args) {
        // 自定义生成JWT令牌的密钥
        String nacosSecret = "nacos_server_secret_key_eugene_forest";
        // 输出密钥长度，要求不得低于32字符，否则无法启动节点。
        System.out.println("密钥长度》》》" + nacosSecret.length());
        // 密钥进行Base64编码
        byte[] data = nacosSecret.getBytes(StandardCharsets.UTF_8);
        System.out.println("密钥Base64编码》》》" + Base64Utils.encodeToString(data));
    }
}
```
````

#### 开启服务身份识别功能

开启鉴权功能后，服务端之间的请求也会通过鉴权系统的影响。考虑到服务端之间的通信应该是可信的，因此在1.2~1.4.0版本期间，通过User-Agent中是否包含Nacos-Server来进行判断请求是否来自其他服务端。

但这种实现由于过于简单且固定，导致可能存在安全问题。因此从1.4.1版本开始，Nacos添加服务身份识别功能，用户可以自行配置服务端的Identity，不再使用User-Agent作为服务端请求的判断标准。

```properties

### 开启鉴权
nacos.core.auth.enabled=true

### 关闭使用user-agent判断服务端请求并放行鉴权的功能
nacos.core.auth.enable.userAgentAuthWhite=false

### 配置自定义身份识别的key（不可为空）和value（不可为空）
nacos.core.auth.server.identity.key=example
nacos.core.auth.server.identity.value=example
```

#### 登录 Nacos 服务，并重置密码

* 打开控制台页面： `http://127.0.0.1:8848/nacos`

此时会跳出登录界面，初次登录的话会进入密码初始化界面，默认，默认账户名为 nacos。

至此 Nacos 初始化完成。

#### 鉴权模式下的 Nacos 服务发现与调用

//TODO: 待补充

## Linux 下配置 Nacos

//TODO: 待补充

### 快速开始（单机模式 + 未开启鉴权）

//TODO: 待补充

### 生产环境部署（集群模式 + 开启鉴权）

//TODO: 待补充

## Nacos 集群模式

//TODO: 待补充

## 扩展: Nacos 配置 mysql数据库

```{tip}

要配置Nacos使用MySQL数据库，请按照以下步骤操作：

* 确认Nacos版本：确保你的Nacos版本是2.2或更高，因为从2.2版本开始，Nacos才开始支持除MySQL和Derby之外的更多数据库类型通过插件的方式。如果版本低于2.2，请先升级Nacos。

* 下载与配置MySQL：确保你已经安装并配置好了MySQL服务器，且版本兼容MySQL5.6及以上协议。

* 获取或开发数据库插件：访问Nacos插件仓库，检查是否已有适用于MySQL的现成插件。对于MySQL而言，实际上并不需要额外的插件，因为Nacos原生支持MySQL。
```

1. 打开Nacos配置文件conf/application.properties，进行以下配置更改

```properties

spring.datasource.platform=mysql
db.num=1
db.url.0=jdbc:mysql://你的数据库地址:端口/nacos?characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true
db.user=你的数据库用户名
db.password=你的数据库密码
```

2. 从 `nacos/conf` 目录下找到 `mysql-schema.sql`（针对Nacos 2.x版本），并使用该SQL脚本在你的MySQL数据库中创建所需的表结构。执行脚本前，请确保你连接的是正确的数据库实例。

3. 完成上述配置后，重新启动Nacos服务。Nacos将使用配置的MySQL数据库作为其数据存储。

## 扩展：Window 环境下封装 Nacos Server 为一个自启动服务

前文我们所有的操作都是基于 CMD 命令行对 Nacos Server 的文件进行指令运行的，那么接下来要说一下如何将这样一个指令封装成一个服务。

> [将 Nacos 转变为 Windows 系统服务](https://developer.aliyun.com/article/1269014)

* 下载 WinSW : WinSW（Windows Service Wrapper 是一个开源的 Windows 服务包装器，它可以帮助你将应用程序打包成系统服务，并实现开机自启动的功能。

* 将 `WinSW-x64.exe` 放在 `nacos/bin` 文件夹下。

* 重命名 `WinSW-x64.exe` 为 `nacos-service.exe` , 并新建一个 `nacos-service.xml` 文件。

* 根据 Nacos 软件包的实际路径编辑 XML 文件

```xml

<service>
<!--  唯一服务ID -->
<id>Nacos</id>
<!--  显示服务的名称  -->
<name>Nacos Service</name>
<!--  服务描述  -->
<description>Nacos 服务</description>
<!--  日志路径 -->
<logpath>D:\LocalService\nacos\bin\logs</logpath>
<!--  日志模式  -->
<logmode>roll</logmode>
<!--  指定启动可执行文件  -->
<executable>D:\LocalService\nacos\bin\startup.cmd</executable>
<!-- 启动参数(-m standalone 单机启动)-->
<arguments>-m standalone</arguments>
<!--  开机启动  -->
<startmode>Automatic</startmode>
<!-- 指定停止可执行文件 -->
<stopexecutable>C:\LocalService\nacos\bin\shutdown.cmd</stopexecutable>
</service>
```

* 在 `nacos\bin` 目录下打开 CMD 命令行，执行以下命令

```cmd

# 安装服务
nacos-service.exe install
# 启动服务
nacos-service.exe start
```

* 在 Windows 系统服务列表可以看到 Nacos 服务；同时登录验证是否开启服务。


````{seealso}

其他命令

```cmd

# 删除服务
nacos-service.exe uninstall
# 查看状态
nacos-service.exe status
# 重启服务
nacos-service.exe restart
```

````
