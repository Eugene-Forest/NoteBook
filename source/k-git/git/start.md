# 准备

(add-github-ssh)=

## 关于在 Git 中添加 Github 的账户的 ssh 密匙

:::{note}

首先，要在本机中创建一个 ssh 密匙，然后在 GitHub 网站中添加公共密匙。最后在本机中验证密匙即可。后续操作中可能会重复使用私有密匙的映射密码验证。
:::

运行下面的命令创建 SSH Key。

```bash
$ ssh-keygen -t rsa -C "your_email@example.com"
Generating public/private rsa key pair.
Enter file in which to save the key
(/Users/your_user_directory/.ssh/id_rsa): 按回车键
Enter passphrase (empty for no passphrase): 输入密码
Enter same passphrase again: 再次输入密码

输入密码后会出现以下结果。
```

:::shell
Your identification has been saved in /Users/your_user_directory/.ssh/id_rsa.
Your public key has been saved in /Users/your_user_directory/.ssh/id_rsa.pub.
The key fingerprint is:
fingerprint值 your_email@example.com
The key's randomart image is:
+--[ RSA 2048]----+
| .+ + |
| = o O . |
略
:::

```{image} ../img/hello_key.png
:alt: hello_key
```

`id_rsa` 文件是私有密钥，`id_rsa.pub` 是公开密钥。

在 GitHub 中添加公开密钥，今后就可以用私有密钥进行认证了。
点击右上角的账户设定按钮（Account Settings），选择 SSH Keys 菜单。点击 Add SSH Key 之后,在 Title 中输入适当的密钥名称。Key 部分请粘贴 `id_rsa.pub` 文件里的内容。

添加成功之后，创建账户时所用的邮箱会接到一封提示“公共密钥添加完成”的邮件。

完成以上设置后，就可以用手中的私人密钥与 GitHub 进行认证和通信了。

```shell
ssh -T git@github.com
```

执行该命令后出现以下结果说明成功。

:::shell
$ ssh -T git@github.com
Enter passphrase for key '/c/Users/qaz22/.ssh/id_rsa':
Hi Eugene-Forest! You've successfully authenticated, but GitHub does not provide shell access.
:::

## 通过 `git bash` 克隆已经创建的仓库，以及添加并提交更新

1. `git add <file_name>`
2. `git commit -m 'commit message'`
3. `git push`

- 通过 `git status` 查看更改状态，通过 `git log` 查看提交情况。

首先，在克隆下的仓库的文件夹下添加文件或更改文件，然后可以执行 `git status` 来查看哪些文件有变动。

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
(use "git add <file>..." to include in what will be committed)
      hello_world.php

nothing added to commit but untracked files present (use "git add" to track)
```

然后执行 `git add <file>` 来被修改或者被添加的文件加入本地暂存，然后再通过 `git commit` 来提交到本地库中。最后再通过 `git push` 命令来更新GitHub仓库。

```bash
$ git add hello_world.php
warning: LF will be replaced by CRLF in hello_world.php.
The file will have its original line endings in your working directory
$ git commit -m 'Add hello_world.php'
[main 1edbabd] Add hello_world.php
1 file changed, 3 insertions(+)
create mode 100644 hello_world.php
$ git push
Enter passphrase for key '/c/Users/qaz22/.ssh/id_rsa':
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 329 bytes | 329.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:Eugene-Forest/Hello-World.git
   d250d0f..1edbabd  main -> main
```
