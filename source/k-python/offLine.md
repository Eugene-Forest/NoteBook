# Python 绿色版及其依赖包的离线安装

> 前情提要：由于公司的开发机器属于内网机，无法联通外网，且又没有类似于 Nexus 仓库作为内网穿透的工具。以下所有操作都是基于 Window 10 的环境。

> -   参考：https://blog.csdn.net/clony1/article/details/112299110
> -   参考：https://www.cnblogs.com/derek-h/p/14849519.html

## Python 绿色版的制作

制作流程大致分为：Python 和 pip 包的下载 -> 将 pip 安装入 Python 包中 -> 加入 pip 安装路径修复工具

-   **Python 离线版的下载**

    -   下载地址：`https://www.python.org/ftp/python/3.7.9/`
    -   下载内容：`python-3.7.9-embed-amd64.zip`

-   **PiP 离线包的安装**

    -   下载地址：`https://pip.pypa.io/en/stable/installing/`
    -   下载内容：在 Installing with get-pip.py 条目下的 get-pip.py 文件
    -   然后在 Python 离线版解压包下与 python.exe 同级目录下运行下方命令 `.\python.exe .\get-pip.py`，会生成两个文件夹。

-   记事本打开 `python37.\_pth`，去除 `import site` 的注释；此时，我们通过运行 `.\Scripts\pip -V` 版本命令来确认是否正常。

    ```{code-block} python

    python37.zip
    .

    # Uncomment to run site.main() automatically
    import site

    ```

## 将 Python 绿色版的包放在其他机器上运行时出现异常

```{code-block} powershell
Fatal error in launcher: Unable to create process using '"D:\MySoftWare\MyPython\python-3.7.9-embed-amd64\python.exe"  "C:\Users\qaz22\Downloads\MyPython\MyPython\python-3.7.9-embed-amd64\Scripts\pip.exe" -V': ???????????
```

这是因为 pip.exe 用绝对路径来找 python，现在换位置了，路径就失效了，通过重新安装可以很容易修复这个错误

> 需要注意，要找到与安装的 pip 包版本相同的修复文件。

下载地址：`https://pypi.tuna.tsinghua.edu.cn/simple/pip/`
下载内容：`pip-23.2.1-py3-none-any.whl`
注意后缀，是 wheel 的文件

将 pip-23.2.1-py3-none-any.whl 文件放在 Python 根目录下，并运行以下命令：

```{code-block} powershell
    .\python -m pip install -U pip-23.2.1-py3-none-any.whl --force-reinstall
```

## 下载 Python 离线依赖包，并在实际的开发机器中安装

> 为什么要在实际开发机器中安装，因为同 pip 的安装一样，如果实现在 Python 绿色版中安装开发依赖，那么也会由于其绝对路径的不同导致无法运行依赖程序，pip 能通过专用的程序进行离线重安装，但是其他的就不一定了，而且从时间成本上来说并不划算。

```{code-block} powershell
    pip download -d your_offline_packages sphinx
```

然后将下载好的依赖重新在新机器上安装

```{code-block} powershell
    .\python -m pip install --no-index --find-links=H:\your_offline_packages sphinx
```

当然，我们会发现，如果我们要初始化一个 Python 环境的时候，一个个依赖地下载和安装费事，可以通过下面的方法来下载和安装：

-   首先，在项目中分析出所有依赖的库 ：

    ```{code-block} powershell
        pip freeze > requirements.txt # 该方法仅可以使用在虚拟环境中，会将 python 解释器下的所有包都导出
    ```

-   将所有包下载到 offLine 这个目录中

    ```{code-block} powershell
        pip download -r requirements.txt -d offLine
    ```

-   将文件打包后放到离线服务器上，并进行解压缩
    ```{code-block} powershell
        pip install --no-index --find-links=d:\python3.6\temp -r requirements.txt
    ```
