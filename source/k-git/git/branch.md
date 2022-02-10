# 分支(branch)篇  特性分支以及分支合并

```{hlist}
:columns: 2

- `git branch`  显示分支一览表
- `git checkout` 切换分支或恢复工作树文件
- `git merge` 合并分支
- `git log --graph`  以图表形式查看分支
- `git stash` 暂存工作目录到脏目录中
```
 
## 列出、创建或删除分支 -- `git branch`

功能对应的可选项：

* 列出分支 `git branch [-a | -r] [--list]` ：如果给了`--list`，或者没有非选项参数，现有的分支将被列出，当前的分支将以绿色突出显示，并标有星号。在链接的工作树中检查出来的任何分支将以青色突出显示，并标有加号。选项`-r`导致远程跟踪的分支被列出，选项`-a`显示本地和远程分支。
* 创建分支： `git branch <newbranch>` 这将创建新的分支，但不会将工作树切换到它；使用 `git switch <newbranch>` 来切换到新的分支。
* 删除分支  `git branch (-d | -D) [-r] <branchname>…​` ：使用`-d`或`-D`选项，*branchname* 将被删除。 你可以指定一个以上的分支进行删除。 如果该分支目前有一个 *reflog* ，那么 *reflog* 也将被删除。使用 `-r` 和 `-d` 来删除远程跟踪的分支。注意，只有当远程分支不再存在于远程仓库或 `git fetch` 被配置为不再获取它们时，删除远程跟踪分支才有意义。参见 `git remote` 的 "prune" 子命令，它可以清理所有过时的远程跟踪分支。
* 重命名分支 `git branch (-m | -M) [<oldbranch>] <newbranch>`​ ：使用`-m`或`-M`选项，*oldbranch* 将被重命名为 *newbranch*。 如果 *oldbranch* 有相应的 *reflog*，它将被重命名以匹配 *newbranch*，并创建一个 *reflog* 条目以记住分支重命名。如果 *newbranch* 存在，必须使用 `-M` 来强制重命名。

```shell
$ git branch
* master

$ git branch feature-A
$ git branch
feature-A
* master

$ git branch # 查看当前所在分支
$ git branch aaa # 新建分支aaa
$ git branch -d aaa # 删除分支aaa
```

分支左侧标有 `*`（星号），表示这我们当前所在的分支。

## 切换分支或恢复工作树文件 -- `git checkout`

关于 `git checkout` 命令，比较常用的可能是创建、切换分支：`git checkout -b <branch>`

```{code-block} shell
:caption: 创建并切换分支

$ git branch feature-A
$ git checkout feature-A
Switched to branch 'feature-A'
..
$ git branch
* feature-A
master

# 当然也可以将创建分支和切换分支合并到同一条命令中
$ git checkout -b feature-A
Switched to branch 'feature-A'
..
$ git branch
* feature-A
master
```

## 切换分支 -- `git switch`

`git switch <branchname>` 切换到指定分支。 


```{warning}

此命令是实验性的。行为可能会改变。

```

## 关于 `git checkout` 与 `git switch` 和 `git restore`

关于 `git restore`,是用来恢复暂存区或工作区文件的， {ref}`点击查看相关笔记 <k-git/git/recall:git restore>` 。

至于 `git switch`, 则是用来切换分支的。

```shell
$ git switch aaa # 切换到 aaa分支
$ git switch -c aaa # 创建aaa，然后切换到 aaa分支
```

而 `git checkout` 则有比较多的用途，而其中一个功能就是切换分支：(由于此命令的功能比较多，所以才出现新版本中的实验命令 `git switch`)

```shell
$ git checkout aaa # 切换到 aaa分支
$ git checkout -b aaa # 创建aaa，然后切换到 aaa分支
```

## Q: 在切换分支前暂存工作分支的变动

当我们切换分支前，可能出现以下情况： 

> 当前工作分支有文件变动，但是又不适合作为一个提交物放在本地库中；而此时，由于工作需要或其他原因，需要前往此仓库的另一个分支。

为了解决这种情况，我们可以使用 `git stash` 命令来将当前工作分支的变动暂存到在脏工作目录中。

调用没有任何参数的 `git stash` 相当于 `git stash save` 。

`git stash pop` 将返回脏工作目录栈中的第一条记录，同时删除。

`git stash drop <stash-name>` 为删除存储命令。


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


## 合并分支 -- `git merge`

```{todo}
待完善, 合并分支可以说是版本控制中最重要的一环之一，它还有许多其他需要注意的地方需要笔记记录。
```


合并分支。

合并有快速合并 `git merge BRANCH_NAME` 以及普通合并 `git merge --no-ff BRANCH_NAME` 之分，区别在于后者可以存在分支合并历史记录，而前者不能。

我们之所以使用版本控制，就是因为需要知道对文件的操作的历史记录，所以笔者更加推荐使用普通合并。（快速合并除了能够带来更加简洁的提交历史记录外毫无意义）

:::{note}

合并分支多半需要进行冲突处理。
:::

## 图表形式查看分支 -- `git log --graph`

以图表形式查看分支。

```shell
$ git log --graph
* commit 83b0b94268675cb715ac6c8a5bc1965938c15f62
|\ Merge: fd0cbf0 8a6c8b9
| | Author: hirocaster <hohtsuka@gmail.com>
| | Date: Sun May 5 16:37:57 2013 +0900
| |
| | Merge branch 'feature-A'
| |
| * commit 8a6c8b97c8962cd44afb69c65f26d6e1a6c088d8
|/ Author: hirocaster <hohtsuka@gmail.com>
| Date: Sun May 5 16:22:02 2013 +0900
|
| Add feature-A
|
* commit fd0cbf0d4a25f747230694d95cac1be72d33441d
| Author: hirocaster <hohtsuka@gmail.com>
| Date: Sun May 5 16:10:15 2013 +0900
|
| Add index
|
* commit 9f129bae19b2c82fb4e98cde5890e52a6c546922
Author: hirocaster <hohtsuka@gmail.com>
Date: Sun May 5 16:06:49 2013 +0900
First commit
```
