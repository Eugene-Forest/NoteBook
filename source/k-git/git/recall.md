# 数据恢复以及返回机制

- `git reset` 回溯历史版本
- `git commit --amend` 修改提交信息
- `git reflog` 查看所有提交，分支变换以及合并等等的操作。
- `git restore`

## git reflog

```shell
$ git reset --hard fd0cbf0d4a25f747230694d95cac1be72d33441d
HEAD is now at fd0cbf0 Add index
```

:::{note}

需要注意的是，当返回到该历史版本之后，在该版本之后的记录会消失，但是可以通过 `git reflog` 命令来查看日志，在其中我们可以看到 commit、checkout、reset、merge 等 Git 命令的执行记录。
:::

```shell
$ git reflog
fd9a51f (HEAD -> main, origin/main) HEAD@{0}: reset: moving to HEAD
fd9a51f (HEAD -> main, origin/main) HEAD@{1}: checkout: moving from feature-A to main
8c80e0b (feature-A) HEAD@{2}: checkout: moving from main to feature-A
fd9a51f (HEAD -> main, origin/main) HEAD@{3}: reset: moving to fd9a51fcf9ed0bdfbaa77cbe8f2f4de8ffcff0b5
6f42ad3 HEAD@{4}: reset: moving to 6f42ad36a86cf2b3774c10f8d96852594258e184
ecc4532 HEAD@{5}: merge feature-A: Merge made by the 'recursive' strategy.
6f42ad3 HEAD@{6}: commit: commit a file whose name is date.txt
fd9a51f (HEAD -> main, origin/main) HEAD@{7}: checkout: moving from feature-A to main
8c80e0b (feature-A) HEAD@{8}: commit: modify README.md in new branch fecture-A.
fd9a51f (HEAD -> main, origin/main) HEAD@{9}: checkout: moving from main to feature-A
fd9a51f (HEAD -> main, origin/main) HEAD@{10}: Branch: renamed refs/heads/main to refs/heads/main
fd9a51f (HEAD -> main, origin/main) HEAD@{12}: reset: moving to HEAD
fd9a51f (HEAD -> main, origin/main) HEAD@{13}: commit (initial): rename a file whose name is eugene.txt to forest.txt
```

## git reset

回溯历史版本。

我们在之前通过 `git log --graph` 查看可知，我们每次提交commit都对应一个哈希值，只要通过命令 `git reset --hard 哈希值` 即可回溯历史版本。

通过 `git reflog` 以及 `git log` 或者 `git log --graph` 获得的日志，可以使用 `git reset` 命令来指定某个哈希值以回到过去的某个状态。

```shell
$ git reset --hard ecc4532
HEAD is now at ecc4532 Merge branch 'feature-A'
```

## git restore

restore命令专门用来恢复staged和worktree的文件。

- `git restore --staged <file>` 命令的效果是将暂存区的某个/某些文件还原到现有的提交(commit)的文件的状态
- `git restore <file>` 命令的效果是将工作区的某个/某些文件还原到现有的暂存区(staged)的文件的状态。
- `git restore --staged --worktree <file>` 命令的效果是将工作区和暂存区的某个/某些文件还原到现有（最新/最近）的提交(commit)的文件的状态

```{image} ../img/git-restore.png
:alt: git restore
```

:::{warning}
记住，在 Git 中任何 **已提交** 的东西几乎总是可以恢复的。 甚至那些被删除的分支中的提交或使用 --amend 选项覆盖的提交也可以恢复。 然而，任何你未提交的东西丢失后很可能再也找不到了。
:::

## git commit --amend 撤销操作

该命令默认撤销的是最新的一次的提交。

```shell
$ git commit --amend
hint: Waiting for your editor to close the file...

[featrue-c 1c8eae6] Rename fecture_c to feature_c, and add a file .gitignore.
Date: Fri Mar 12 15:30:28 2021 +0800
2 files changed, 15 insertions(+)
create mode 100644 .gitignore
rename fecture_c => feature_c (100%)
```

这个命令会将暂存区中的文件提交。 如果自上次提交以来你还未做任何修改（例如，在上次提交后马上执行了此命令）， 那么快照会保持不变，而你所修改的只是提交信息。
文本编辑器启动后，可以看到之前的提交信息。 **编辑后保存会覆盖原来的提交信息**。

:::{warning}
记住，在 Git 中任何 已提交 的东西几乎总是可以恢复的。 甚至那些被删除的分支中的提交或使用 --amend 选项覆盖的提交也可以恢复。 然而，任何你未提交的东西丢失后很可能再也找不到了。
:::
