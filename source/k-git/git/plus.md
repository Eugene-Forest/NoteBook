# 忽略文件以及文件控制系统的特殊操作

## 关于忽略文件(.gitignore)

文件 .gitignore 的格式规范如下：

- 所有空行或者以 # 开头的行都会被 Git 忽略。
- 可以使用标准的 glob 模式匹配，它会递归地应用在整个工作区中。
- 匹配模式可以以（/）开头防止递归。
- 匹配模式可以以（/）结尾指定目录。
- 要忽略指定模式以外的文件或目录，可以在模式前加上叹号（!）取反。

:::{note}

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。

星号（\*）匹配零个或多个任意字符；\[abc\] 匹配任何一个列在方括号中的字符 （这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）。

问号（?）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符， 表示所有在这两个字符范围内的都可以匹配（比如 \[0-9\] 表示匹配所有 0 到 9 的数字）。

使用两个星号（\*\*）表示匹配任意中间目录，比如 a/\*\*/z 可以匹配 a/z 、 a/b/z 或 a/b/c/z 等。
:::

```shell
#   忽略所有的 .a 文件
*.a
# 但跟踪所有的 lib.a，即便你在前面忽略了 .a 文件
!lib.a
# 只忽略当前目录下的 TODO 文件，而不忽略 subdir/TODO
/TODO
# 忽略任何目录下名为 build 的文件夹
build/
# 忽略 doc/notes.txt，但不忽略 doc/server/arch.txt
doc/*.txt
# 忽略 doc/ 目录及其所有子目录下的 .pdf 文件
doc/**/*.pdf
```

:::{note}

.gitignore文件通用模板

```{literalinclude} ./.gitignore
```

:::

## 关于移除文件的操作

在这里，需要了解一下 `git rm` 以及 `git restore` 这两个命令。

其中， `git restore --staged <file>` 命令的效果是将暂存区的某个/某些文件还原到现有的提交(commit)的文件的状态， `git restore <file>` 命令的效果是将工作区的某个/某些文件还原到现有的暂存区(staged)的文件的状态。

```{image} ../img/git-restore.png
:alt: git restore
```

:::{note}

简而言之， `git restore` 命令是用来恢复文件的。
:::

git rm 命令用于删除文件。
如果只是简单地从工作目录中手工删除文件，运行 git status 时就会在 Changes not staged for commit 的提示。

git rm 删除文件有以下几种形式：

1. 将文件从暂存区和工作区中删除：`git rm <file>`
2. 如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f: `git rm -f <file>`
3. 如果想把文件从暂存区域移除，但仍然希望保留在当前工作目录中，换句话说，仅是从跟踪清单中删除，使用 --cached 选项即可: `git rm --cached <file>`

```shell
$ git status
On branch featrue-c
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
      new file:   .gitignore
      modified:   fecture_c
$ git rm fecture_c
error: the following file has changes staged in the index:
   fecture_c
(use --cached to keep the file, or -f to force removal)
$ ls
README.md  date.txt  fecture_c  forest.txt  peng/  pwq
$ git rm -f fecture_c
rm 'fecture_c'
$ ls
README.md  date.txt  forest.txt  peng/  pwq
$ git diff

$ git diff --cached
diff --git a/fecture_c b/fecture_c
deleted file mode 100644
index d2ad9d8..0000000
--- a/fecture_c
+++ /dev/null
@@ -1 +0,0 @@
-In this file, I will tell you some message about the new fecture. Actually, you can think of it as a new README.MD at fecture-c.

$ git restore --staged --worktree fecture_c
$ ls
README.md  date.txt  fecture_c  forest.txt  peng/  pwq
$ git diff
$ git diff --cached
```

```shell
$ git rm --cached fecture_c
rm 'fecture_c'
$ ls
README.md  date.txt  fecture_c  forest.txt  peng/  pwq
$ git diff

$ git diff --cached
diff --git a/fecture_c b/fecture_c
deleted file mode 100644
index d2ad9d8..0000000
--- a/fecture_c
+++ /dev/null
@@ -1 +0,0 @@
-In this file, I will tell you some message about the new fecture. Actually, you can think of it as a new README.MD at fecture-c.

$ git status
On branch featrue-c
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
      new file:   .gitignore
      deleted:    fecture_c

Untracked files:
(use "git add <file>..." to include in what will be committed)
      fecture_c
```

:::{warning}
记住，在 Git 中任何 **已提交** 的东西几乎总是可以恢复的。 甚至那些被删除的分支中的提交或使用 --amend 选项覆盖的提交也可以恢复。 然而，任何你未提交的东西丢失后很可能再也找不到了。
:::

## 关于移动(重命名)文件的操作

:::{note}

不像其它的 VCS 系统，Git 并不显式跟踪文件移动操作。 如果在 Git 中重命名了某个文件，仓库中存储的元数据并不会体现出这是一次改名操作。 不过 Git 非常聪明，它会推断出究竟发生了什么。
:::

使用 `git mv FILENAME_FORM FILENAME_TO` 命令。

:::{warning}
需要注意的是，`git mv` 命令是同时对暂存区以及工作区的文件进行修改，这意味着当被重命名的文件没有被追踪， *不需要也不要使用该命令*，只需要使用 `mv` 命令即可。
:::

```shell
$ git status
On branch featrue-c
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
      new file:   .gitignore
      deleted:    fecture_c

Untracked files:
(use "git add <file>..." to include in what will be committed)
      fecture_c
$ ls
README.md  date.txt  fecture_c  forest.txt  peng/  pwq
$ git mv fecture_c feature_c
fatal: not under version control, source=fecture_c, destination=feature_c

$ git add .
$ git mv fecture_c feature_c
$ ls
README.md  date.txt  feature_c  forest.txt  peng/  pwq
$ git diff
$ git diff --cached
...
diff --git a/fecture_c b/feature_c
similarity index 100%
rename from fecture_c
rename to feature_c

$ git status
On branch featrue-c
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
      new file:   .gitignore
      renamed:    fecture_c -> feature_c
```
