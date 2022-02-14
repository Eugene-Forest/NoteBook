# 扩展

:::{note}

较少用但是比较实用的技术。
:::

## git stash [^id5]

`git stash`（git储藏）可用于以下情形：

* 发现有一个类是多余的，想删掉它又担心以后需要查看它的代码，想保存它但又不想增加一个脏的提交。这时就可以考虑 `git stash`。

* 使用 git 的时候，我们往往使用分支（branch）解决任务切换问题，例如，我们往往会建一个自己的分支去修改和调试代码, 如果别人或者自己发现原有的分支上有个不得不修改的 bug ，我们往往会把完成一半的代码 commit 提交到本地仓库，然后切换分支去修改 bug ，改好之后再切换回来。这样的话往往 `log` 上会有大量不必要的记录。其实如果我们不想提交完成一半或者不完善的代码，但是却不得不去修改一个紧急 Bug ，那么使用 `git stash` 就可以将你当前未提交到本地（和服务器）的代码推入到 Git 的栈中，这时候你的工作区间和上一次提交的内容是完全一样的，所以你可以放心的修 Bug ，等到修完 Bug ，提交到服务器上后，再使用 `git stash apply` 将以前一半的工作应用回来。

* 经常有这样的事情发生，当你正在进行项目中某一部分的工作，里面的东西处于一个比较杂乱的状态，而你想转到其他分支上进行一些工作。问题是，你不想提交进行了一半的工作，否则以后你无法回到这个工作点。解决这个问题的办法就是 `git stash` 命令。储藏(stash)可以获取你工作目录的中间状态——也就是你修改过的被追踪的文件和暂存的变更——并将它保存到一个未完结变更的堆栈中，随时可以重新应用。


当要记录工作目录和索引的当前状态，但想要返回到干净的工作目录时，则使用 `git stash` 。 该命令保存本地修改，并恢复工作目录以匹配 HEAD 提交。

这个命令所储藏的修改可以使用 `git stash list` 列出，使用 `git stash show` 进行检查，并使用 `git stash apply` 恢复(可能在不同的提交之上)。 默认情况下，储藏列表为“分支名称上的WIP”，但您可以在创建一个消息时在命令行上给出更具描述性的消息。如果你想应用更早的储藏，可以通过名字指定它，像这样： `git stash apply stash@{2}` 。如果不指明，Git 默认使用最近的储藏并尝试应用它。


* `git stash` : 保存本地修改，并恢复工作目录以匹配HEAD提交。将会把存储放在存储队列的队头中。
* `git stash -m "message"` : 默认情况下，储藏列表为  “WIP on 分支名: \<default message\>” ，但你可以在创建一个消息时在命令行上添加选项参数 `-m` 来给出更具描述性的消息。将会把存储放在存储队列的队头中。
* `git stash save` : 调用没有任何参数的 `git stash` 相当于 `git stash save` 。将会把存储放在存储队列的队头中。
* `git stash show [stash-name]` : 存储内容与创建此存储项时的提交状态之间的差异。
* `git stash list` : 展示当前存储库中的存储队列。每个元素包含的信息有索引位置,存储时所在的分支,存储前的提交的描述。
* `git stash apply <stash-name>` : 如果你想应用更早的储藏，可以通过名字指定它，像这样： `git stash apply stash@{2}`
* `git stash pop` : 使用最近的储藏（即*stash@{0}*）并删除它
* `git stash drop <stash-name>` : 删除指定存储的命令。
* `git stash clear` : 删除所有缓存的stash。

````{admonition} 注意
:class: important

需要注意的是，`git stash show` 显示的是创建此存储项时的提交状态之间的差异，也就是说这个 `git stash show` 显示的值是不会变的。同时如果有注意到的话我们可以发现 `git stash list` 可以出现不同分支中的存储(如下 *代码块 git stash list*)，这说明本地仓库中的所有分支共用一个脏存储队列。

创建的最新储藏存储在 `.git` 目录下的 `refs/stash` 中。

```{code-block} shell
:caption: git stash list

$ git stash list
stash@{0}: On b-doc: add a file named doc-file.md
stash@{1}: On main: save the main-file-1.md
stash@{2}: WIP on main: 4a5fae0 add fest
```
````

### 实例1

当你处于某种状态的时候，你会发现有一些上游的变化可能与正在做的事情有关。当您的本地更改不会与上游的更改冲突时，简单的 `git pull` 将让您向前。
但是，有些情况下，本地更改与上游更改相冲突， `git pull` 拒绝覆盖您的更改。 在这种情况下，您可以将更改隐藏起来，执行  `git pull` ，然后重新获取本地更改解决冲突，如下所示：


```shell
git pull
...
file foobar not up to date, cannot merge.
$ git stash
$ git pull
$ git stash pop
```

### 实例2

当你处于某种状态的时候，比如你的老板进来，要求立即开会或处理非常紧急的事务。 传统上，应该提交一个临时分支来存储您的更改，并返回到原始(original)分支进行紧急修复，如下所示:

```shell
# ... hack hack hack ...
$ git checkout -b my_wip
$ git commit -a -m "WIP"
$ git checkout master
$ edit emergency fix # 编辑内容
$ git commit -a -m "Fix in a hurry"
$ git checkout my_wip
$ git reset --soft HEAD^
# ... continue hacking ...
```

上面过程可以使用 `git stash` 来简化上述操作，如下所示：

```shell
# ... hack hack hack ...
$ git stash
$ edit emergency fix
$ git commit -a -m "Fix in a hurry"
$ git stash pop
# ... continue hacking ...
```



## 从其他分支中获取文件

```{todo}
应当添加到 git checkout 的详解篇章中
```

```{code-block} git
:caption: 从其他分支中获取文件

git checkout source_branch <paths>
```

此命令会从目标分支中获取指定文件，并添加或覆盖到当前分支中。一般来说，路径以项目的根目录为起始。




 
[^id5]: 原文出自【易百教程】，原文链接：<https://www.yiibai.com/git/git_stash.html>
