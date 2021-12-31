# Q: windows平台下使用git add，git deploy 文件时经常出现“warning: LF will be replaced by CRLF” 的提示

```bash
$ git add README.md
warning: LF will be replaced by CRLF in README.md.
The file will have its original line endings in your working directory
```
 
本文链接：<https://blog.csdn.net/wq6ylg08/article/details/88761581>
 
## 分析了解CR and CRLF

1. 不同操作系统下，处理行尾结束符的方法是不同的：

   1. Windows和Dos下：使用回车（CR）和换行（LF）两个字符来结束一行，回车+换行(CR+LF)，即“\\r\\n”；
   2. Unix和mac下：只使用换行（LF）一个字符来结束一行，即“\\n”；

   - (最早Mac每行结尾是回车CR 即'\\r'，后mac os x 也投奔了 unix)

2. Git下处理“换行”（line ending）
   core.autocrlf是git中负责处理line ending的变量，可以设置3个值：true，false，input。

   - 设置为true【`config --global core.autocrlf true`】
     : 当设置成true时，这意味着你在任何时候添加(add)文件到git仓库时，git都会视为它是一个文本文件(text file)。它将把crlf变成LF。
   - 设置为false【`config --global core.autocrlf false`】
     : 当设置成false时，line endings将不做转换操作。文本文件保持原来的样子。
   - 设置为input【`config --global core.autocrlf input`】
     : 设置为input时，添加文件git仓库时，git把crlf编程lf。当有人Check代码时还是lf方式。因此在window操作系统下，不要使用这个设置。

## 此问题的负面影响

:::{warning}
格式化与多余的空白字符，特别是在跨平台情况下，有时候是一个令人发指的问题。由于编辑器的不同或者文件行尾的换行符在 Windows 下被替换了，一些细微的空格变化会不经意地混入提交，造成麻烦。虽然这是小问题，但会极大地扰乱跨平台协作。
:::

假如你正在Windows上写程序;又或者你正在和其他人合作，他们在Windows上编程，而你却在其他系统上，在这些情况下，你可能会遇到行尾结束符问题。此问题的全部负面影响如下：

(1)一个直接后果是，Unix/Mac系统下的一个“多行文本”文件在Windows里打开的话，“多行文本”会变成“一行”。（原因：Unix/Mac换行只用了换行符‘\\n’，而Windows的换行要求是回车换行符’\\r\\n’，因此Unix/Mac中的“多行文本”的换行不符合Windows的规则，所以Windows对这些不符合换行规则的“多行文本”全部按照“没有换行”处理，所以导致“多行文本”会变成“一行”）

(2)而Windows里的文件在Unix/Mac下打开的话，在每行的结尾可能会多出一个^M符号。

(3)Linux保存的文件在windows上用记事本看的话会出现黑点。

## 解决此问题的方案

1. 如果我们目前是Window平台并出现该警告，啥也别做就行，虽然这个警告难看，但这个警告能保证我们项目团队正常跨系统git操作代码

   因为git的Windows 客户端基本都会默认设置 core.autocrlf=true（我们可通过git config core.autocrlf命令查询我们的Windows上该属性是否默认true。如不是true,通过config --global core.autocrlf true命令设置该属性为true），而“core.autocrlf=true”有以下3个功能来避免我们出错：

   - 在“把 modified修改过的文件git add到暂存区stage”时，Git自动把LF转换成CRLF,并给出那条警告”LF will be replaced by CRLF”
   - 在“把modified修改过的文件由暂存区(stage) 提交(commit)到版本库/仓库(repository)”时，Git自动把CRLF转换成LF
   - 在“用 检出/git checkout切换到指定分支 或 git clone克隆远程版本库”来加载代码时，Git自动把LF转换成CRLF

2. 如果我们是Linux 或 Mac平台,我们不需要功能“在检出或克隆远程版本库时，Git自动把LF转换成CRLF”。然而当一个CRLF作为行结束符的文件在我们的Linux 或 Mac平台不小心被引入时，你肯定想让 Git 修正。 所以，你可以通过config --global core.autocrlf input命令把 core.autocrlf 设置成 input 来告诉 Git 在提交(commit)时把CRLF转换成LF，检出(git checkout)时不转换

:::{note}

提到的那句警告：“IF will be replaced by CRLF in \<file-name>”

这句警告的下面其实还有一句很重要的话：The file will have its original line endings in your working directory.

(翻译："在工作区里，这个文件会保留它原本的换行符")
:::

这样在 Windows 上的检出(checkout)文件中会保留CRLF，而在 Mac 和 Linux 上，以及版本库中会保留LF，从而保证我们项目团队正常跨系统git操作代码。
