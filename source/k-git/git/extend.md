# 扩展

:::{note}

较少用但是比较实用的技术。
:::
 
当我们切换分支前，可能有以下几种情况：（当前分支--> 目标分支）

1. 所有在当前分支的修改与变动都已经提交到本地git仓库中（即使用 `git diff` 以及 `git diff --staged` 都是没有内容）。

2. 所有在当前分支的修改与变动没有提交到本地git仓库中，只保留在工作树或暂存区中。

   - 所有在当前分支的修改与变动都已经暂存到本地暂存区中
   - 所有在当前分支的修改与变动都未暂存或提交到 git 仓库中，只保留在工作树中
   - 当前分支的修改与变动一部分暂存到本地暂存区中，另一部分保留在工作树中。

对于第一种情况，我们不需要加以讨论；我们着重说明第二种情况，这种情况可以分一下两种情形讨论：

- 一种情形，如果两个分支之间变动的文件没有交集（不涉及文件具体内容的修改，目前可以明确为文件的添加或删除），那么是可以直接不提交当前分支的修改与变动直接切换分支，但是这样便意味着当前分支的对文件的增删会影响到目标分支，一般不会期望这种情况发生。
- 另一种情形，如果两个分支之间变动的文件出现交集，例如当前分支与目标分支有同一个文件，且当前分支恰好对该文件进行内容上的修改，那么无法直接切换分支的，需要将当前分支的变动提交(commit)后才可以切换分支。

*一般来说，我们在切换前将当前分支的变动和修改提交到仓库即可，这样可以避免许多意料之外的事情。*

那么，出现一种情况——我们需要切换分支，但是又不想将当前分支当前状态的工作树提交（commit）为一个版本记录这种情况的时候，我们可应当如何处理？这就可以使用 `git stash` ！

## git stash [^id5]

当要记录工作目录和索引的当前状态，但想要返回到干净的工作目录时，则使用git stash。 该命令保存本地修改，并恢复工作目录以匹配HEAD提交。

这个命令所储藏的修改可以使用 `git stash list` 列出，使用 `git stash show` 进行检查，并使用 `git stash apply` 恢复(可能在不同的提交之上)。 默认情况下，储藏列表为“分支名称上的WIP”，但您可以在创建一个消息时在命令行上给出更具描述性的消息。如果你想应用更早的储藏，可以通过名字指定它，像这样： `git stash apply stash@{2}` 。如果不指明，Git 默认使用最近的储藏并尝试应用它。

调用没有任何参数的 `git stash` 相当于 `git stash save` 。

`git stash drop <stash-name>` 为删除存储命令。

创建的最新储藏存储在refs/stash中; 这个引用的反垃圾邮件中会发现较旧的垃圾邮件，并且可以使用通常的reflog语法命名(例如，<mailto:stash@{0>}是最近创建的垃圾邮件，<mailto:stash@{1>}是stash@{2.hours.ago}之前也是可能的)。也可以通过指定存储空间索引(例如整数n相当于储藏stash@\{n})来引用锁存。

### 实例1

当你处于某种状态的时候，你会发现有一些上游的变化可能与正在做的事情有关。当您的本地更改不会与上游的更改冲突时，简单的 `git pull` 将让您向前。
但是，有些情况下，本地更改与上游更改相冲突， `git pull` 拒绝覆盖您的更改。 在这种情况下，您可以将更改隐藏起来，执行  `git pull` ，然后解压缩，如下所示：

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
 
## other

other content
 
[^id5]: 原文出自【易百教程】，原文链接：<https://www.yiibai.com/git/git_stash.html>