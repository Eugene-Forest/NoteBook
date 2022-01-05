# 工作区的插件设置

VSCode是一款免费开源的现代化轻量级代码编辑器，支持几乎所有主流的开发语言的语法高亮、智能代码补全、自定义快捷键、括号匹配和颜色区分、代码片段、代码对比 Diff、GIT命令等特性，同时也是非常重要的是VSCode**支持插件扩展**。

## `.code-workspace` 文件

```{figure} ../img/vs-code/workspace/workspace-file.png
:align: center
:alt: workspace-file

工作区示例
```

关于工作区配置文件：

* `.code-workspace` 的文件名就是工作区的名字。
* `.code-workspace` 的文件中定义了 根目录（`.code-workspace` 的所属的文件夹）中哪些文件或文件夹属于此工作区。
* `.code-workspace` 中使用的一些插件的配置。

```{code-block} json
:caption: 工作区配置文件

{
    "folders": [
    // 将载入到工作区的文件夹列表
        {
            "path": "."
        }
    ],
    "settings": {
    // 工作区设置
    }
}
```

## 特定工作区使用特定插件集

VSCode 的一个目标是轻量级，但是随着我们的使用，VSCode 会被安装到许多插件，而太多的插件会使得 VSCode 变得臃肿，甚至运行变慢，占用太多内存，所以此文章介绍了工作区，并如何来使用工作区更好地体验 VSCode。

**如果是第一次使用工作区来激活特定插件，那么可以在建完工作区后将所有插件禁用，然后再把需要的插件 启用(工作区) 。**

```{figure} ../img/vs-code/workspace/disable-all-plugin.png
:align: center
:alt: disable-all-plugin

禁用所有插件（用户设置）
```

```{figure} ../img/vs-code/workspace/active-plugin-workspace.png
:alt: active-plugin-workspace.png
:align: center

找到目标插件，将其再此工作区中激活
```

```{figure} ../img/vs-code/workspace/active-plugin-workspace-status.png
:alt: active-plugin-workspace.png
:align: center

插件在工作区中激活后的状态
```

````{note}

需要注意的是，我们再安装新的插件的时候，它默认是全局启用的。所以如果在配置完不同工作区的激活插件后，还想要安装插件，那么需要注意在**安装此插件后先禁用全局使用，然后再预期的工作区中激活此插件**。

```{figure} ../img/vs-code/workspace/code-spell-checker-global.png
:alt: code-spell-checker-global.png
:align: center

插件安装后的默认状态
```
````
