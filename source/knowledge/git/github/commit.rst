======================
分支（branch） 二
======================

* ``git reset`` 回溯历史版本
* ``git commit --amend`` 修改提交信息
* ``git rebase -i`` 压缩历史
* ``git reflog`` 查看所有提交，分支变换以及合并等等的操作。


----

git reset
--------------

回溯历史版本。

我们再通过 ``git log --graph`` 查看可知，我们每次提交commit都对应一个哈希值，只要通过命令 ``git reset --hard 哈希值`` 即可回溯历史版本。

git reflog
---------------

.. code-block:: shell

   $ git reset --hard fd0cbf0d4a25f747230694d95cac1be72d33441d
   HEAD is now at fd0cbf0 Add index

.. note:: 
   需要注意的是，当返回到该历史版本之后，在该版本之后的记录会消失，但是可以通过 ``git reflog`` 命令来查看日志，在其中我们可以看到 commit、checkout、reset、merge 等 Git 命令的执行记录。

.. code-block:: shell

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

通过该日志，可以使用git reset 命令来指定某个哈希值以回到过去的某个状态。

.. code-block:: shell

   $ git reset --hard ecc4532
   HEAD is now at ecc4532 Merge branch 'feature-A'

----

git 