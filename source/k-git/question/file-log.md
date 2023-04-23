# 文件或文件夹的 git 提交历史

> 有时候，我们会遇到一种情况，就是需要查看某个文件的在某段时间之后的历史提交/修改，或者是某个文件夹下的所有文件的历史修改记录，这个时候，如果我们通过全局的历史提交来判断某个文件的变动，那么效率极低。

## `git log [fileName/dirName]`

通过在 git log 命令后面添加文件名或文件夹的名字，可以获取此文件夹或文件的所有的提交记录。

```git

$ ls
Makefile  README.md  RemoteGitee.md  make.bat  source/


$ git log
commit 022c10aba0a15a9a8b1d1551ac4383301cbbbf97 (HEAD -> main, gitee/main)
Author: Eugene-Forest <1244303915@qq.com>
Date: Thu Aug 11 01:15:49 2022 +0000

    add RemoteGitee.md.

commit 7ca4df262dddc5b2a5812c6e2b42142dff19d589
Author: Eugene-Forest <1244303915@qq.com>
Date: Fri Dec 24 09:42:08 2021 +0800

    init


$ git log RemoteGitee.md
commit 022c10aba0a15a9a8b1d1551ac4383301cbbbf97 (HEAD -> main, gitee/main)
Author: Eugene-Forest <1244303915@qq.com>
Date:   Thu Aug 11 01:15:49 2022 +0000

    add RemoteGitee.md.


$ git log source
commit 7ca4df262dddc5b2a5812c6e2b42142dff19d589
Author: Eugene-Forest <1244303915@qq.com>
Date:   Fri Dec 24 09:42:08 2021 +0800

    init


```
