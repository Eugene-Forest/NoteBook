(sphinx-ext-autobuild)=

# sphinx-autobuild

> **更新时间: 2021-12-21, 11:46:56  | sphinx_autobuild 版本：{{sphinx_autobuild}}**

在浏览器中实时重新加载有关更改的 Sphinx 文档。关于此项目的更多信息或建议前往 [executablebooks/sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild#readme) 查看。

## 安装

`sphinx-autobuild` 在 **PyPI** 上可用。它可以使用 pip 安装：

```shell
pip install sphinx-autobuild
```

## 用法

要构建经典的 Sphinx 文档集，请运行：

```shell
sphinx-autobuild source source/_build/html
```

这将在 `http://127.0.0.1:8000` 启动服务器并开始监视 `source/` 目录中的更改。当在 `source/` 中检测到更改时，将重建文档并自动重新加载任何打开的浏览器窗口，而结果则输出在 `source/_build/html` 中。

使用 KeyboardInterrupt( `ctrl+ c`) 停止服务器。

````{admonition} 推荐用法
```shell
sphinx-autobuild source source/_build/html --open-browser --port=0
```

当然，可以将其写入批处理文件中，这样就可以直接执行：

```{code-block} shell
:caption: .sh 批处理

#!/bin/sh
sphinx-autobuild source source/_build/html --open-browser --port=0
```

```{code-block} powershell
:caption: .bat 批处理

sphinx-autobuild source source/_build/html --open-browser --port=0
```

````

## 命令行选项

`sphinx-autobuild` 接受与 `sphinx-build`（这些在每次构建时传递给 `sphinx-build` ）相同的参数。它还有一些额外的选项，可以通过运行看到 `sphinx-autobuild --help`

```shell
$ sphinx-autobuild --help
usage: sphinx-autobuild [-h] [--port PORT] [--host HOST] [--re-ignore RE_IGNORE] [--ignore IGNORE] [--no-initial] [--open-browser]
                        [--delay DELAY] [--watch DIR] [--pre-build COMMAND] [--version]
                        sourcedir outdir [filenames [filenames ...]]

positional arguments:
  sourcedir             source directory
  outdir                output directory for built documentation
  filenames             specific files to rebuild on each run (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           port to serve documentation on. 0 means find and use a free port (default: 8000)
  --host HOST           hostname to serve documentation on (default: 127.0.0.1)
  --re-ignore RE_IGNORE
                        regular expression for files to ignore, when watching for changes (default: [])
  --ignore IGNORE       glob expression for files to ignore, when watching for changes (default: [])
  --no-initial          skip the initial build (default: False)
  --open-browser        open the browser after building documentation (default: False)
  --delay DELAY         how long to wait before opening the browser (default: 5)
  --watch DIR           additional directories to watch (default: [])
  --pre-build COMMAND   additional command(s) to run prior to building the documentation (default: [])
  --version             show program's version number and exit

sphinx's arguments:
  The following arguments are forwarded as-is to Sphinx. Please look at `sphinx --help` for more information.
    -b=builder, -a, -E, -d=path, -j=N, -c=path, -C, -D=setting=value, -t=tag, -A=name=value, -n, -v, -q, -Q, -w=file, -W, -T, -N, -P
```

## 自动打开浏览器

sphinx-autobuild 可以在默认浏览器中打开生成文档的主页。通过 `--open-browser` 将启用此行为。

## 自动选择端口

sphinx-autobuild 要求操作系统提供一个空闲端口号并将其用于其服务器。通过 `--port=0` 将启用此行为。
