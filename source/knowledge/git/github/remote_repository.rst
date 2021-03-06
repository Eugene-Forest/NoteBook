========================================
与远程仓库*remote repository* 的交互
========================================


首先，在github中创建一个空的同名仓库，然后获得远程仓库的链接(形如 *git@github.com:Eugene-Forest/Forest.git* )后，再通过命令将本地的仓库内容添加到远程仓库中。


添加远程仓库之一：create a new repository on the command line
------------------------------------------------------------------

.. code-block:: shell

   echo "# Forest" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git branch -M master
   git remote add origin git@github.com:Eugene-Forest/Forest.git
   git push -u origin master

.. note:: 运行 ``git remote add <shortname> <url>`` 添加一个新的远程 Git 仓库，同时指定一个方便使用的简写。如上代码所示，即可使用origin来代替 *git@github.com:Eugene-Forest/Forest.git* 这个URL。

添加远程仓库之二：push an existing repository from the command line
----------------------------------------------------------------------

.. code-block:: shell

   git remote add origin git@github.com:Eugene-Forest/Forest.git
   git branch -M master
   git push -u origin master

添加远程仓库之三：clone
---------------------------------------

.. code-block:: shell

   git clone git@github.com:Eugene-Forest/Forest.git

查看远程仓库
-----------------

使用 ``git remote`` 命令即可查看本地仓库的远程仓库。
如果想要查看某一个远程仓库的更多信息，可以使用 ``git remote show <remote>`` 命令。

.. code-block:: shell

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

从远程仓库中抓取与拉取
----------------------------

.. code-block:: shell

   $ git fetch <remote>


推送到远程仓库
----------------------

.. code-block:: shell

   git push <remote> <branch>

.. note:: 

   `Git push与pull的默认行为 <https://segmentfault.com/a/1190000002783245>`_ 

远程仓库的重命名
--------------------

.. code-block:: shell

   git remote rename BRANCH_NAME_FROM BRANCH_NAME_TO

值得注意的是这同样也会修改你所有远程跟踪的分支名字。

远程仓库的移除
--------------------

.. code-block:: shell

   git remote remove repo_name # git remote rm repo_name
