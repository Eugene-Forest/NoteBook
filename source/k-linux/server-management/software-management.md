# 软件及其服务管理篇

:::{note}

本篇主要记录在centos7中的软件管理。且这些软件都是通过 {ref}`阿里yum源 <config-ali-yum>`  安装的。
:::

1. 软件管理

   1. 更新本地yum源 `yum makecache`
   2. 搜索软件 `yum search SOFTWARE-NAME`
   3. 安装软件 `yum install SOFTWARE-NAME`
   4. 卸载软件 `yum remove SOFTWARE-NAME`

2. 服务管理

   1. 开启服务/启动软件 `systemctl start SOFTWARE-NAME/Server-Name`
   2. 查看软件/服务运行状态 `systemctl status SOFTWARE-NAME/Server-Name`
   3. 停止软件/服务运行 `systemctl stop SOFTWARE-NAME/Server-Name`
   4. 软件/服务开机自启动 `systemctl enable SOFTWARE-NAME/Server-Name`

3. 软件信息查看

   1. 查看是否已安装及其安装版本 `yum list installed | grep SOFTWARE-NAME`
   2. 查看软件安装位置及其相关文件路径 `whereis SOFTWARE-NAME`
