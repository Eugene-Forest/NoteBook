# 与远程仓库 *remote repository* 的交互

首先，在 Github 中创建一个空的同名仓库，然后获得远程仓库的链接(形如 *git@github.com:Eugene-Forest/Forest.git* )后，再通过命令将本地的仓库内容添加到远程仓库中。

## 添加远程仓库之一：*create a new repository on the command line*

添加一个新的远程 Git 仓库 `git remote add <shortname> <url>`

```shell
echo "# Forest" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin git@github.com:Eugene-Forest/Forest.git
git push -u origin master
```

:::{note}

运行 `git remote add <shortname> <url>` 添加一个新的远程 Git 仓库，同时指定一个方便使用的简写。如上代码所示，即可使用origin来代替 *git@github.com:Eugene-Forest/Forest.git* 这个URL。
:::

## 添加远程仓库之二：*push an existing repository from the command line*

```shell
git remote add origin git@github.com:Eugene-Forest/Forest.git
git branch -M master
git push -u origin master
```

## 添加远程仓库之三：*clone*

```shell
git clone git@github.com:Eugene-Forest/Forest.git
```

## 查看远程仓库

使用 `git remote` 命令即可查看本地仓库的远程仓库。
如果想要查看某一个远程仓库的更多信息，可以使用 `git remote show <remote>` 命令。

```shell
$ git remote
origin
$ git remote -v
origin  git@github.com:Eugene-Forest/GitRepositoryManual.git (fetch)
origin  git@github.com:Eugene-Forest/GitRepositoryManual.git (push)
$ git remote show origin
Enter passphrase for key '/c/xxxx/.ssh/id_rsa':
* remote origin
Fetch URL: git@github.com:Eugene-Forest/GitRepositoryManual.git
Push  URL: git@github.com:Eugene-Forest/GitRepositoryManual.git
HEAD branch: main
Remote branch:
   main tracked
Local branch configured for 'git pull':
   main merges with remote main
Local ref configured for 'git push':
   main pushes to main (fast-forwardable)
```

## 从远程仓库中抓取与拉取

```shell
$ git fetch <remote>
```

## 推送到远程仓库

```shell
git push <remote> <branch>
```

:::{note}

[Git push与pull的默认行为](https://segmentfault.com/a/1190000002783245)
:::

## 远程仓库的重命名

```shell
git remote rename BRANCH_NAME_FROM BRANCH_NAME_TO
```

值得注意的是这同样也会修改你所有远程跟踪的分支名字。

## 远程仓库链接的修改

`git remote set-url <repo_name> <new_url>`

```bash
> git remote -v
gitee   https://gitee.com/eugene-forest/NoteBook.git (fetch)
gitee   https://gitee.com/eugene-forest/NoteBook.git (push)
origin  git@github.com:Eugene-Forest/NoteBook.git (fetch)
origin  git@github.com:Eugene-Forest/NoteBook.git (push)
> git remote set-url gitee git@github.com:Eugene-Forest/NoteBook.git
> git remote -v
gitee   git@github.com:Eugene-Forest/NoteBook.git (fetch)
gitee   git@github.com:Eugene-Forest/NoteBook.git (push)
origin  git@github.com:Eugene-Forest/NoteBook.git (fetch)
origin  git@github.com:Eugene-Forest/NoteBook.git (push)
```

## 远程仓库链接的附加

如果我们由两个远程仓库，而且在推送时都想同时向这两个远程仓库推送，那么这个时候，可以使用 `git remote set-url --add <repo_name> <other-url>` 命令。

```shell
> git remote -v
origin  git@github.com:Eugene-Forest/NoteBook.git (fetch)
origin  git@github.com:Eugene-Forest/NoteBook.git (push)
> git remote set-url --add origin https://gitee.com/eugene-forest/NoteBook.git
> git remote -v
origin  git@github.com:Eugene-Forest/NoteBook.git (fetch)
origin  git@github.com:Eugene-Forest/NoteBook.git (push)
origin  https://gitee.com/eugene-forest/NoteBook.git (push)
```

:::{note}

从运行结果来看，通过 `git remote set-url --add <repo_name> <other-url>` 命令添加的远程仓库只有被推送的权利，当我们向远程拉取的时候还是一开始的远程仓库。
:::

## 远程仓库的移除

```shell
git remote remove repo_name # git remote rm repo_name
```


## 查看远程仓库的分支并拉取到本地


* 通过 `git branch -a` 命令可以查看所有的无论是本地还是远程的分支。
* 通过 `git branch -r` 命令可以查看所有的远程的分支。

* `git checkout -b LOCAL_BRANCH_NAME REMOTE_NAME/REMOTE_BRANCH_NAME` 在本地新建分支并从远程拉取，采用此种方法建立的本地分支会和远程分支建立映射关系。
* `git fetch origin REMOTE_BRANCH_NAME:LOCAL_BRANCH_NAME` 在本地新建分支并从远程拉取，这种方法建立的本地分支不会和远程分支建立映射关系。


## 本地分支与远程分支的映射关系

* `git branch -vv` 查看本地分支与远程分支的映射关系

    ```{code-block} bash

    Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-git/repository/GitOperationManual (main)
    $ git branch -vv
    feature-a b4ef42a a test for diff feature delete files
    * main      022c10a [gitee/main] add RemoteGitee.md.
    ```

* 本地分支与远程分支的映射关系的撤销 `git branch --unset-upstream`

    ```{code-block} bash

    Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-git/repository/GitOperationManual (main)
    $ git branch --unset-upstream

    Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-git/repository/GitOperationManual (main)
    $ git branch -vv
    feature-a b4ef42a a test for diff feature delete files
    * main      022c10a add RemoteGitee.md.
    ```

* 本地分支与远程分支的映射关系的建立

  * `git branch -u REMOTE_NAME/REMOTE_BRANCH_NAME`

  * `git branch --set-upstream-to=REMOTE_NAME/REMOTE_BRANCH_NAME`

   ```{code-block} bash

    Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-git/repository/GitOperationManual (main)
    $ git branch --set-upstream-to=gitee/main
    Branch 'main' set up to track remote branch 'main' from 'gitee'.

    Eugene-Forest@DESKTOP-4BMMHQP MINGW64 ~/workspace-git/repository/GitOperationManual (main)
    $ git branch -vv
    feature-a b4ef42a a test for diff feature delete files
    * main      022c10a [gitee/main] add RemoteGitee.md.

   ```
