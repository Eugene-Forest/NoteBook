# 标签的使用 [^id7]

tag 用于创建一个标签 用于在开发阶段，某个阶段的完成，创建一个版本，在开发中都会使用到, 可以创建一个tag来指向软件开发中的一个关键时期，比如版本号更新的时候可以建一个version1.0,  version1.2之类的标签，这样在以后回顾的时候会比较方便。tag的使用很简单。

`git tag` 命令用于创建，列出，删除或验证使用GPG签名的标签对象。

## 列显已有的标签

`git tag | git tag -l <expression>`

## 创建轻量级标签

`git tag <tag-name>`

## 删除标签

`git tag -d <tag-name>`

## 查看某标签的信息

`git show <tag-name>`


## 推送标签信息
 

默认情况下，`git push` 并不会把标签传送到远端服务器上，只有通过显式命令才能分享标签到远端仓库。其命令格式如同推送分支，运行 `git push origin [tagname]` 即可：


```{code-block} bash

$ git push origin v1.5
Counting objects: 50, done.
Compressing objects: 100% (38/38), done.
Writing objects: 100% (44/44), 4.56 KiB, done.
Total 44 (delta 18), reused 8 (delta 1)
To git@github.com:schacon/simplegit.git
* [new tag]         v1.5 -> v1.5
```

如果要一次性推送所有标签，可以使用 `--tag` 选项:

```{code-block} bash
$ git push origin --tags
Counting objects: 50, done.
Compressing objects: 100% (38/38), done.
Writing objects: 100% (44/44), 4.56 KiB, done.
Total 44 (delta 18), reused 8 (delta 1)
To git@github.com:schacon/simplegit.git
 * [new tag]         v0.1 -> v0.1
 * [new tag]         v1.2 -> v1.2
 * [new tag]         v1.4 -> v1.4
 * [new tag]         v1.4-lw -> v1.4-lw
 * [new tag]         v1.5 -> v1.5
```




[^id7]: 原文出自【易百教程】，原文链接：<https://www.yiibai.com/git/git_tag.html>
