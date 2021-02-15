
======
准备
======

关于在git中添加ssh密匙
------------------------

.. note:: 

   首先，要在本机中创建一个ssh密匙，然后在GitHub网站中添加公共密匙。最后在本机中验证密匙即可。后续操作中可能会重复使用私有密匙的映射密码验证。

运行下面的命令创建 SSH Key。

.. code-block:: bash

   $ ssh-keygen -t rsa -C "your_email@example.com"
   Generating public/private rsa key pair.
   Enter file in which to save the key
   (/Users/your_user_directory/.ssh/id_rsa): 按回车键
   Enter passphrase (empty for no passphrase): 输入密码
   Enter same passphrase again: 再次输入密码

   输入密码后会出现以下结果。

.. code-block:: shell

   Your identification has been saved in /Users/your_user_directory/.ssh/id_rsa.
   Your public key has been saved in /Users/your_user_directory/.ssh/id_rsa.pub.
   The key fingerprint is:
   fingerprint值 your_email@example.com
   The key's randomart image is:
   +--[ RSA 2048]----+
   | .+ + |
   | = o O . |
   略


.. image:: ../../../img/hello_key.png
   :alt: hello_key

id_rsa 文件是私有密钥，id_rsa.pub 是公开密钥。

在 GitHub 中添加公开密钥，今后就可以用私有密钥进行认证了。
点击右上角的账户设定按钮（Account Settings），选择 SSH Keys 菜单。点击 Add SSH Key 之后,在 Title 中输入适当的密钥名称。Key 部分请粘贴 id_rsa.pub 文件里的内容。

添加成功之后，创建账户时所用的邮箱会接到一封提示“公共密钥添加完成”的邮件。

完成以上设置后，就可以用手中的私人密钥与 GitHub 进行认证和通信了。

.. code-block:: shell

   $ ssh -T git@github.com

执行该命令后出现以下结果说明成功。

.. code-block:: shell

   $ ssh -T git@github.com
   Enter passphrase for key '/c/Users/qaz22/.ssh/id_rsa':
   Hi Eugene-Forest! You've successfully authenticated, but GitHub does not provide shell access.
