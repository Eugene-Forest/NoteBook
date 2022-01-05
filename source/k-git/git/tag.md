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
 
[^id7]: 原文出自【易百教程】，原文链接：<https://www.yiibai.com/git/git_tag.html>
