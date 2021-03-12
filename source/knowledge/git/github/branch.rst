=============================================
分支(branch)篇 一 特性分支以及分支合并
=============================================

* ``git branch``  显示分支一览表
* ``git checkout -b``  创建并切换分支
* ``git merge`` 合并分支
* ``git log --graph``  以图表形式查看分支

----

git branch
--------------

显示分支一览表或者创建一个新的分支。


.. code-block:: shell

   $ git branch
   * master

.. code-block:: shell

   $ git branch feature-A
   $ git branch
   feature-A
   * master

分支左侧标有“*”（星号），表示这我们当前所在的分支。

.. note:: 
   通过git branch命令还可以删除指定分支， 只需要添加参数 -d；如： ``git branch -d BRANCH_NAME``

git checkout -b
--------------------------------

创建、切换分支。

.. code-block:: shell

   $ git branch feature-A
   $ git checkout feature-A
   Switched to branch 'feature-A'
   ..
   $ git branch
   * feature-A
   master

.. code-block:: shell

   $ git checkout -b feature-A
   Switched to branch 'feature-A'
   ..
   $ git branch
   * feature-A
   master

以上两段代码实现的功能都是创建并切换分支。


git merge
------------------

合并分支。

合并有快速合并 ``git merge BRANCH_NAME`` 以及普通合并 ``git merge --no-ff BRANCH_NAME`` 之分，区别在于后者可以存在分支合并历史记录，而前者不能。

.. note:: 
   合并分支多半需要进行冲突处理。

git log --graph
------------------------

以图表形式查看分支。

.. code-block:: shell

   $ git log --graph
   * commit 83b0b94268675cb715ac6c8a5bc1965938c15f62
   |\ Merge: fd0cbf0 8a6c8b9
   | | Author: hirocaster <hohtsuka@gmail.com>
   | | Date: Sun May 5 16:37:57 2013 +0900
   | |
   | | Merge branch 'feature-A'
   | |
   | * commit 8a6c8b97c8962cd44afb69c65f26d6e1a6c088d8
   |/ Author: hirocaster <hohtsuka@gmail.com>
   | Date: Sun May 5 16:22:02 2013 +0900
   |
   | Add feature-A
   |
   * commit fd0cbf0d4a25f747230694d95cac1be72d33441d
   | Author: hirocaster <hohtsuka@gmail.com>
   | Date: Sun May 5 16:10:15 2013 +0900
   |
   | Add index
   |
   * commit 9f129bae19b2c82fb4e98cde5890e52a6c546922
   Author: hirocaster <hohtsuka@gmail.com>
   Date: Sun May 5 16:06:49 2013 +0900
   First commit



----

关于 ``git checkout`` 与 ``git switch`` 和 ``git restore``
------------------------------------------------------------

关于 ``git restore``, :ref:`点击查看相关笔记 <git-restore>` 。

