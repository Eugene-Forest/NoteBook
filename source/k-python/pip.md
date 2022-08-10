# pip 命令详解

`pip` 是 `Python` 包管理工具，该工具提供了对 `Python` 包的查找、下载、安装、卸载的功能。

目前如果你在 [python.org](https://www.python.org/) 下载最新版本的安装包，则是已经自带了该工具。

可以通过以下命令来判断是否已安装：

```{code-block} python
:caption: pip 版本命令
pip --version     # Python2.x 版本命令
pip3 --version    # Python3.x 版本命令
```

## 安装 pip

一般来说，在 *Windows* 环境下的 *Python* 安装一般都同时安装了 `pip` 工具，所以在本篇章中不说明如何在 *Windows* 下安装 `pip` ；如果由此需要，建议前往[官网](https://www.python.org/)直接重新安装 *Python* 。

如果还未安装，则可以使用以下方法来安装：

```{code-block} shell
:caption: Linux 环境下安装 pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
# 哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本
$ sudo python3 get-pip.py   # 运行安装脚本
```

## pip 常用命令


```{admonition} pip 与 pip3
:class: important

在 Linux 中，由于需要支撑其内核，所以操作系统中一般会默认有 Python 的 2.x 版本。而由于一些 Python 包不能向前兼容 Python 2.x ，需要我们安装 Python 3.x 版本。这样一来，我们就会发现在一个操作系统中存在两个 Python 和 pip 工具。这个时候，我们一般认为命令 python 和 pip 指的是 2.x 版本的，而 python3 和 pip3 是 3.x 版本的。

在 Windows 中，如果也安装了两个大版本的 Python ，那么处理方法也同上。
```

```{hlist}
:columns: 2

* 显示版本和路径 : `pip -V` or `pip --version`
* 获取帮助 : `pip -h` or `pip --help`
* 升级pip : `pip install -U pip`
* 安装包 : `pip install some_package`
* 升级包 : `pip install --upgrade some_package`
* 卸载包 : `pip uninstall some_package`
* 搜索包 : `pip search some_package`
* 显示安装包信息 : `pip show some_package`
* 查看指定包的详细信息 : `pip show -f some_package`
* 列出已安装的包 : `pip list`
* 查看可升级的包 ： `pip list -o`
```

### 升级pip

```{code-block} python
:caption: Linux 或 macOS
pip install --upgrade pip    # python2.x
pip3 install --upgrade pip   # python3.x
```

```{code-block} python
:caption: Windows 平台
python -m pip install -U pip   # python2.x
python3 -m pip3 install -U pip    # python3.x
```

### 安装包

通过使用==, >=, <=, >, < 来指定一个版本号。

```{code-block} python
:caption: 安装包
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
```

### 升级包

升级指定的包，同样可以通过使用==, >=, <=, >, < 来指定一个版本号。

```{code-block} python
:caption: 升级包
pip install --upgrade SomePackage==1.7
```


## 镜像

默认情况下 pip 使用的是国外的镜像，在下载的时候速度非常慢，介绍使用国内清华大学的源，地址为： `https://pypi.tuna.tsinghua.edu.cn/simple`

### 临时使用清华大学镜像来安装包

我们可以直接在 `pip` 命令中使用 `-i` 参数来指定镜像地址：

```{code-block} python
:caption: "临时使用清华大学镜像"

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

### 设清华大学镜像为默认

升级 `pip` 到最新的版本 (>=10.0.0) 后进行配置：

```{code-block} python
:caption: "设清华大学镜像为默认"

pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果到 `pip` 默认源的网络连接较差，临时使用清华大学镜像镜像站来升级 `pip` ：

```{code-block} python
:caption: "临时使用清华大学镜像镜像站来升级 pip"

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```


```
> pip config list

> pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
Writing to C:\Users\qaz22\AppData\Roaming\pip\pip.ini

> pip config list
global.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'

```

````{admonition} 修改配置文件来设置默认镜像

*Linux* 下，找到配置文件 `~/.pip/pip.conf` ,并添加或修改配置属性成如下所示：

```{code-block} guess
:caption:  Linux 下配置
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

*Windows* 下，你需要在当前对用户目录下的 `pip.ini` 文件（`C:\Users\xx....\pip\pip.ini`) 【如果没有就创建一个 `pip.ini`】添加或修改配置属性成如下所示：

```{code-block} guess
:caption: Windows下配置
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

````
