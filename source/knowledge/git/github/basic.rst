===========
git basic
===========

.. image:: ../../../img/git-command.jpg
   :alt: git-command

* workspace：工作区
* staging area：暂存区/缓存区
* local repository：版本库或本地仓库
* remote repository：远程仓库

Git 常用的是以下 6 个命令：

* ``git clone``
* ``git push``
* ``git add`` 
* ``git commit``
* ``git checkout``
* ``git pull``

----

介绍如何通过git bash创建一个存储库并进行基本操作。

* ``git init`` 初始化仓库
* ``git status`` 查看仓库的状态
* ``git add`` 向暂存区添加文件
* ``git commit`` 将暂存区的文件添加到仓库中
* ``git log`` 查看提交历史
* ``git diff`` 查看更改前后的差异

----

初始化仓库--git status
------------------------

实际建立一个目录并初始化仓库

.. code-block:: bash

   $ mkdir GitRepositoryManual
   $ cd GitRepositoryManual
   $ git init
   Initialized empty Git repository in /c/Users/qaz22/GitRepository
   /GitRepositoryManual/.git/

.. note:: 

   在 Git 中，我们将 ``.git`` 这个目录的内容称为“附属于该仓库的工作树”。文件的编辑等操作在工作树中进行，然后记录到仓库中，以此管理文件的历史快照。( **.git** 文件夹内的文件可以认为是对仓库操作的日志文件)

查看仓库状态--git status
-----------------------------

工作树和仓库在被操作的过程中，状态会不断发生变化。在 Git 操作过程中时常用 git status命令查看当前状态。(*会显示当前分支*)

.. code-block:: shell

   $ git status
   On branch main

   No commits yet

   nothing to commit (create/copy files and use "git add" to track)


向暂存区中添加文件--git add ( ``git add .`` :将工作区的所有变动的文件提交到暂存区)
-------------------------------------------------------------------------------------

.. code-block:: shell

   $ git add README.md
   $ git status
   # On branch main
   #
   # Initial commit
   #
   # Changes to be committed:
   # (use "git rm --cached <file>..." to unstage)
   #
   # new file: README.md
   #

保存到仓库----git commit
--------------------------------

git commit命令可以将当前暂存区中的文件实际保存到仓库的历史记录中。通过这些记录，我们就可以在工作树中复原文件。

不妨养成这样一个好习惯：在执行 ``git commit`` 命令之前先执行 ``git diff HEAD`` 命令，查看本次提交与上次提交之间有什么差别，等确认完毕后再进行提交。