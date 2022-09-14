# 代码模板

通过定义和使用代码模板来提高工作效率与代码可预测性的能力。我们在使用 Idea 、 Vs Code 等主流 IDE 或编辑器的时候，一般都有相关的代码提示的插件。

一般来说，软件预置的代码提示的代码模板都是常见、普通和可预见的。

当我们有特殊的代码模板需求的时候无法满足时，有必要了解一下代码模板。

## 关于 Vs Code 下的代码模板 [^vscode-code-template]

如果需要在 Vs Code 中使用自定义代码模板，我们可以在工作区或者项目根目录下的 `.vscode` 文件夹下添加模板文件。

### 创建 snippets

* 菜单栏选择 `File` / `文件`
* 下拉菜单中选择 `Preferences` / `首选项`
* 再选择 `User snippets` / `配置用户代码片段` ，出现下图情况，选择对应的语言即可；如果没有你需要的语言，你需要安装对应的语言插件

点击配置用户代码片段并弹出选项后，我们可以看到有两种选择，一种是针对全局的代码模板（json文件形式），另一种是针对工作区的代码模板（code-snippets文件形式）。

```{code-block} json

{
    "For_Loop": {
        "prefix": "for",
        "body": [
          "for (const ${2:element} of ${1:array}) {",
          "\t$0",
          "}"
        ],
        "description": "For Loop"
    }
}

```

* `For_Loop` : 当前 snippet 名字。
* `prefix` : 前缀，代码块使用快捷方式；键入前缀，按 *tab* 键，代码块就会被使用。
* `body` : 代码块内容；换行使用 `\r\n` ，或直接使用如例子所示的字符串分段换行。
* `description` : 键入前缀， *vscode* 感知到前缀，显示的说明内容。
* `$1,$2,$0` : 指定代码模块生成后，编辑光标出现位置; 使用 *Tab* 键进行切换(编辑光标按 `$1,$2,$3...$0` 的顺序跳转)， `$0` 是光标最后可切换位置。

## Snippet语法

### Tabstops

`$1，$2` 是指定代码块生成后，光标出现的位置；不同位置出现相同 `$1` ，那么这些位置会同时出现光标。

### Placeholders

给光标出现位置加上默认值；例如，`${1:another ${2:placeholder}}`；$1处位置默认值是another。

### Choice

光标位置设置多个值可供选择; 例如，`${1|one,two,three|}`；`$1` 位置处可以选择 `one,two,three` 中一个词填充在此处。

### Variables

* 日期和时间相关变量
  * `CURRENT_YEAR` 当前年
  * `CURRENT_YEAR_SHORT` 当前年后两位
  * `CURRENT_MONTH` 月份，两位数字表示，例如02
  * `CURRENT_MONTH_NAME` 月份全称，例如 'July'
  * `CURRENT_MONTH_NAME_SHORT` 月份简写 ，例如'Jul
  * `CURRENT_DATE` 某天
  * `CURRENT_DAY_NAME` 星期几， 例如'Monday')
  * `CURRENT_DAY_NAME_SHORT` 星期几的简写， 'Mon'
  * `CURRENT_HOUR` 小时，24小时制
  * `CURRENT_MINUTE` 分钟
  * `CURRENT_SECOND` 秒数

* 常用变量
  * `TM_SELECTED_TEXT` 当前选中内容或空字符串
  * `TM_CURRENT_LINE` 当前行内容
  * `TM_CURRENT_WORD` 光标处字符或空字符串
  * `TM_LINE_INDEX` 从0开始的行号
  * `TM_LINE_NUMBER` 从1开始的行号
  * `TM_FILENAME` 当前被编辑文档名
  * `TM_FILENAME_BASE` 当前被编辑文档名，没有后缀
  * `TM_DIRECTORY` 当前被编辑文档目录
  * `TM_FILEPATH` 当前被编辑文档全路径
  * `CLIPBOARD` 当前剪切板内容

----

[^vscode-code-template]: 引用自 [【简书】VSCode 添加代码模板——作者：JeremyL](https://www.jianshu.com/p/07a7fd95954f)
