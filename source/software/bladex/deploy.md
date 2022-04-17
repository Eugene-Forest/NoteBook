# Spring Blade 项目部署

本章节将讲解如何在 **Linux** 环境下部署 **Spring Blade** （后端 **boot** 版本 + 前端 **saber** 版本）前后端项目。

## 后端项目的部署

后端项目主要要注意 `application.yml` 和 `application-dev.yml`（根据实际情况） 的配置，当然如果你的项目的运行环境不是 ``dev`` 而是其他的例如 ``prod`` ，那么就应该看你的 `application.yml` 和 `application-prod.yml` 的配置 。

根据配置文件确认一下信息：

* 服务端口
* redis 密码
* 数据库信息

在这里，建议本地开发使用的环境为 dev ，打包使用正式环境 prod；这样就不用在需要打包时改动本地运行配置。

由于 Spring Blade 的启动模块默认无环境指定的情况下运行 dev 环境，所以我们在打包之后部署（运行 jar 包）需要在命令行添加指令参数 `--spring.profiles.active=prod` 

相关运行命令如下所示：

* 在当前终端运行 jar 包 `java -jar SpringBlade.jar --spring.profiles.active=prod`

* 当前终端运行 jar 包，同时退出当前终端不会结束此进程 `nohup java -jar SpringBlade.jar --spring.profiles.active=prod >temp.txt &` 

* 查看jar运行的程序 `ps -ef | grep java`

* 杀死进程 `kill -9 <pid>`



### 关于后端的跨域问题的配置

Spring Blade 官方文档提供的方法：**SpringBoot Cors 配置**

```{code-block} java
@Configuration
public class BladeConfiguration implements WebMvcConfigurer {

   @Override
   public void addCorsMappings(CorsRegistry registry) {
      registry.addMapping("/**")
         .allowedOrigins("*")
         .allowedHeaders("*")
         .allowedMethods("*")
         .maxAge(3600)
         .allowCredentials(true);
   }

}
```

```{note} 

此方法笔者未使用，但是理论上是可行且最简单的。

```

## 前端项目的部署和跨域问题的解决

前端项目基本只需要对 `vue.config.js` 进行修改完善即可：

项目运行 npm run build 获取 dist 构建文件（夹）。并将文件夹内的内容放到 nginx 的资源文件路径下 /usr/share/nginx/html （替换了原来的内容）。

*资源文件的放置路径因人而异。*

### 项目反向代理配置

```{code-block} js
  devServer: {
    // 端口配置；根据实际需要，对应nginx中的监听端口
    port: 80,
    // 反向代理配置
    proxy: {
      '/api/*': {
        target: 'http://127.0.0.1:8080',
        //target url ,注意端口
        ws: false,
        changeOrigin: true, //支持跨域
        pathRewrite: {
          '^/api': '/api'
        }
      }
    },
  },
```


### nginx 反向代理配置

关于 nginx 的配置只需要对需要被监听的前端端口进行如下配置即可。

```
server {
        server_name  localhost;
        # root 路径指向项目
        root         /usr/share/nginx/html;
        # 监听端口，这里对应前端
        listen       80;
        # Load configuration files for the default server block.
       include /etc/nginx/default.d/*.conf;
       
        location / {
            # root 路径指向项目
            root  /usr/share/nginx/html;
            index  index.html index.htm;
        }


     location ^~ /api/ {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_buffering off;
            rewrite ^/api/(.*)$ /$1 break;
            # 代理指向注意端口以及http类型，这里指向后端服务，所以端口需要对应
            proxy_pass http://pengweiquan.top:8080;
        }

    }
```

## 关于 SSL 证书的添加

接下来说明一个简单的 SSL 证书添加的实现，当然前提是有自己的域名。

在这里，笔者使用的是阿里云服务器和域名，以及在阿里云中免费申请的 SSL 证书。

### Spring boot 项目的 SSL 证书的添加

先在阿里云中下载 tomcat 版本的证书，并参考阿里云官方提供的文档进行配置 [在Spring Boot上启用HTTPS](https://help.aliyun.com/document_detail/365559.html) ：

我们下载并解压后会获得两个文件：

* 证书文件（domain name.pfx）
* 密码文件（pfx-password.txt）

然后将解压后的证书文件和密码文件拷贝到 *Spring Boot* 项目的根目录 `src/main/resources/` 下。

```{note}
如果您修改过 *Spring Boot* 项目的目录，您需要将证书文件和密码文件拷贝到与配置文 `application.properties` 或 `application.yml` 相同的目录下。
```

接下来，需要修改配置文件 `application.properties` 或 `application.yml` 。

```{code-block} guess
:caption: application.properties 下的配置

server.port = 443    #HTTPS协议默认端口号为443，需要使用其他端口时，您可以在此处自定义。
server.ssl.key-store: classpath = <domain name.pfx>   #您需要使用实际的证书名称替换domain name.pfx。
server.ssl.key-store-password = ********    #填写pfx-password.txt文件内的密码。
server.ssl.keyStoreType = PKCS12
```

```{code-block} yml
:caption: application.yml 下的配置

server:
  port: 443    #HTTPS协议默认端口号为443，需要使用其他端口时，您可以在此处自定义。
  ssl:
    key-alias: tomcat   # 需要根据证书文件的实际别名
    key-store-password: ********    #填写pfx-password.txt文件内的密码。
    key-store-type: PKCS12
    key-store: classpath:<domain name.pfx>    #您需要使用实际的证书名称替换domain name.pfx。
```

在这里，基本只需要参考其文档即可完成配置，但是需要注意的是 yml 配置文件中的密匙别名需要对应实际；先到达证书文件目录下，然后命令： `keytool -list -v -keystore <domain name.pfx>` ，查看别名。

```{code-block} powershell

C:\Users\qaz22\Downloads\7610256_domain name_tomcat>keytool -list -v -keystore domain name.pfx
输入密钥库口令:
密钥库类型: PKCS12
密钥库提供方: SunJSSE

您的密钥库包含 1 个条目

别名: alias
创建日期: 2022-4-15
条目类型: xxxxxxxxxxxxxxxxx
证书链长度: 2
证书[1]:
所有者: CN=domain name
发布者: CN=xxxxxxxxxxxxxxxxxxxxxx
序列号: xxxxxxxxxxxxxxxxxxxxxxxxx
生效时间: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
证书指纹:
         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
签名算法名称: xxxxxxxxxxxxxxxxxxx
主体公共密钥算法: 2048 位 RSA 密钥
版本: 3

....
```

### nginx 服务器的 SSL 证书添加

参考阿里云文档 [在Nginx（或Tengine）服务器上安装证书](https://help.aliyun.com/document_detail/98728.html) 。

执行以下命令，在 **Nginx** 安装目录（笔者为 `/ect/nginx/` ）下创建一个用于存放证书的目录，将其命名为 **cert** 。【即 *nginx.config* 文件所在的目录下新建一个用于放置证书文件的目录 **cert** 。】

将证书文件放入 **cert** 目录下，然后编辑 **Nginx** 配置文件（*nginx.conf*），修改与证书相关的配置内容:


```

server {
    listen 80;
    server_name  www.pengweiquan.top;#需要将yourdomain替换成证书绑定的域名。
    rewrite ^(.*)$ https://$host$1; #将所有HTTP请求通过rewrite指令重定向到HTTPS。
    location / {
        index index.html index.htm;
    }
}

#以下属性中，以ssl开头的属性表示与证书配置有关。
server {
    listen 443 ssl;
    #配置HTTPS的默认访问端口为443。
    #如果未在此处配置HTTPS的默认访问端口，可能会造成Nginx无法启动。
    #如果您使用Nginx 1.15.0及以上版本，请使用listen 443 ssl代替listen 443和ssl on。
    server_name www.pengweiquan.top; #需要将yourdomain替换成证书绑定的域名。

    # 替换为项目实际路径
    root /usr/share/nginx/html;
    index index.html index.htm;

    ssl_certificate cert/7610256_www.pengweiquan.top.pem;  #需要将cert-file-name.pem替换成已上传的证书文件的名称。
    ssl_certificate_key cert/7610256_www.pengweiquan.top.key; #需要将cert-file-name.key替换成已上传的证书私钥文件的名称。
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    #表示使用的加密套件的类型。
    ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3; #表示使用的TLS协议的类型。
    ssl_prefer_server_ciphers on;

        location / {
            # 替换为项目实际路径
            root  /usr/share/nginx/html;
            index  index.html index.htm;
        }


     location ^~ /api/ {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_buffering off;
            rewrite ^/api/(.*)$ /$1 break;
            # 替换为后端接口路径
            proxy_pass https://www.pengweiquan.top:8080;
        }

}

```
