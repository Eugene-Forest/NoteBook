# RST-to-MyST

一种转换 [ReStructuredText](https://docutils.sourceforge.io/) 为 [MyST Markdown](https://myst-parser.readthedocs.io/) 的工具。

```{seealso}
更多相关使用的信息可查看 [RST-to-MyST的官方文档](https://rst-to-myst.readthedocs.io/en/latest/index.html)。
```

**目前，转换指令时指令的参数或选项会出现中文乱码的问题。**

## Getting Started

从PyPI安装:

```shell
pip install "rst-to-myst[sphinx]"
```

建议在隔离的环境中安装。
其中一种方法是使用 [pipx](https://pypa.github.io/pipx/):

```console
$ pipx install "rst-to-myst[sphinx]"
$ pipx list
venvs are in /Users/username/.local/pipx/venvs
apps are exposed on your $PATH at /Users/username/.local/bin
   package rst-to-myst 0.1.2, Python 3.7.3
    - rst2myst
```

然后运行整个项目的基本转换:

```console
$ rst2myst convert docs/**/*.rst
```

为了更好的控制，你可以通过CLI选项传递配置，或者通过YAML配置文件:

```console
$ rst2myst convert --config config.yaml docs/**/*.rst
```

`config.yaml`:

```yaml
language: en
sphinx: true
extensions:
- sphinx_panels
default_domain: py
consecutive_numbering: true
colon_fences: true
dollar_math: true
conversions:
    sphinx_panels.dropdpwn.DropdownDirective: parse_all
```
