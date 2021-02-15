============
最基本操作
============


通过git bash克隆已经创建的仓库，以及添加并提交更新
---------------------------------------------------

#. ``git add <file_name>``
#. ``git commit -m 'commit message'``
#. ``git push``

* 通过 ``git status`` 查看更改状态，通过 ``git log`` 查看提交情况。

----

首先，在克隆下的仓库的文件夹下添加文件或更改文件，然后可以执行 ``git status`` 来查看哪些文件有变动。

.. code-block:: bash

   $ git status
   On branch main
   Your branch is up to date with 'origin/main'.

   Untracked files:
   (use "git add <file>..." to include in what will be committed)
         hello_world.php

   nothing added to commit but untracked files present (use "git add" to track)

然后执行 ``git add <file>`` 来被修改或者被添加的文件加入本地暂存，然后再通过 ``git commit`` 来提交到本地库中。最后再通过 ``git push`` 命令来更新GitHub仓库。

.. code-block:: bash

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
