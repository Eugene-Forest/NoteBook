# @profile 注解

(note-profile)=

@profile注解是spring提供的一个用来标明当前运行环境的注解。

Profile的意思是配置，对于应用程序来说，不同的环境需要不同的配置。
比如：

- 开发环境，应用需要连接一个可供调试的数据库单机进程
- 生产环境，应用需要使用正式发布的数据库，通常是高可用的集群
- 测试环境，应用只需要使用内存式的模拟数据库

Spring框架提供了多profile的管理功能，我们可以使用profile功能来区分不同环境的配置。

:::{warning}
笔者推荐博客 [解读 Spring Profile 的用法](https://www.cnblogs.com/huahua-test/p/11576907.html)
:::

% // todo @profile to be continued
