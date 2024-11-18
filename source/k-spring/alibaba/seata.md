# Seata

[Spring Boot 分布式事务 Seata 入门](https://www.cnblogs.com/cj8357475/p/16361477.html)

目前两个用例都是直接访问 seata server 的方式进行全局事务回滚的；

由于此项目用例用到了 nacos 来发现和注册 seata server 的服务配置；

## seata 的配置相关

### seata-server/conf/application.yml 参考

```yaml

server:
  port: 7091

spring:
  application:
    name: seata-server

logging:
  config: classpath:logback-spring.xml
  file:
    path: E:\LocalService\apache-seata-2.2.0-incubating-bin\seata-server\logs\seata
  extend:
    logstash-appender:
      destination: 127.0.0.1:4560
    kafka-appender:
      bootstrap-servers: 127.0.0.1:9092
      topic: logback_to_logstash

console:
  user:
    username: seata
    password: seata
seata:
  config:
    # support: nacos, consul, apollo, zk, etcd3
    type: nacos
    nacos:
      server-addr: 127.0.0.1:8848
      namespace:
      group: SEATA_GROUP
      context-path:
      ##1.The following configuration is for the open source version of Nacos
      username:
      password:
      ##2.The following configuration is for the MSE Nacos on aliyun
      #access-key:
      #secret-key:
      ##3.The following configuration is used to deploy on Aliyun ECS or ACK without authentication
      #ram-role-name:
      data-id: seataServer.properties
  registry:
    # support: nacos, eureka, redis, zk, consul, etcd3, sofa
    type: nacos
    nacos:
      application: seata-server
      server-addr: 127.0.0.1:8848
      group: SEATA_GROUP
      namespace:
      cluster: default
      context-path:
      ##1.The following configuration is for the open source version of Nacos
      username:
      password:
      ##2.The following configuration is for the MSE Nacos on aliyun
      #access-key:
      #secret-key:
      ##3.The following configuration is used to deploy on Aliyun ECS or ACK without authentication
      #ram-role-name:
  store:
    # support: file 、 db 、 redis 、 raft
    mode: db
  #  server:
  #    service-port: 8091 #If not configured, the default is '${server.port} + 1000'
  security:
    secretKey: SeataSecretKey0c382ef121d778043159209298fd40bf3850a017
    tokenValidityInMilliseconds: 1800000
    csrf-ignore-urls: /metadata/v1/**
    ignore:
      urls: /,/**/*.css,/**/*.js,/**/*.html,/**/*.map,/**/*.svg,/**/*.png,/**/*.jpeg,/**/*.ico,/api/v1/auth/login,/version.json,/health,/error,/vgroup/v1/**
```



需要特别提示， 

* `server.port=7091` 的配置一般不需要更改；这个端口是用来登录事务管理后台界面的，真正的 seata-server 在下方的 seata.server.service-port
* `seata.server.service-port` 默认端口号是 server.port 端口号 +1000 的值，如果有相关端口更改需要特别留意。
* `seata.config.nacos...`, 指定了 从 nacos 服务中获取的 seataServer.properties 配置文件
* 如果 nacos 开启了鉴权，那么需要填写对应的账号密码。

### seataServer.properties

```properties

#For details about configuration items, see https://seata.apache.org/zh-cn/docs/user/configurations
#Transport configuration, for client and server
transport.type=TCP
transport.server=NIO
transport.heartbeat=true
transport.enableTmClientBatchSendRequest=false
transport.enableRmClientBatchSendRequest=true
transport.enableTcServerBatchSendResponse=false
transport.rpcRmRequestTimeout=30000
transport.rpcTmRequestTimeout=30000
transport.rpcTcRequestTimeout=30000
transport.threadFactory.bossThreadPrefix=NettyBoss
transport.threadFactory.workerThreadPrefix=NettyServerNIOWorker
transport.threadFactory.serverExecutorThreadPrefix=NettyServerBizHandler
transport.threadFactory.shareBossWorker=false
transport.threadFactory.clientSelectorThreadPrefix=NettyClientSelector
transport.threadFactory.clientSelectorThreadSize=1
transport.threadFactory.clientWorkerThreadPrefix=NettyClientWorkerThread
transport.threadFactory.bossThreadSize=1
transport.threadFactory.workerThreadSize=default
transport.shutdown.wait=3
transport.serialization=seata
transport.compressor=none

#Transaction routing rules configuration, only for the client
# 特别注意 service.vgroupMapping
service.vgroupMapping.default_tx_group=default
service.vgroupMapping.tutor_datasource_group=default
service.vgroupMapping.account_service_group=default
service.vgroupMapping.product_service_group=default
service.vgroupMapping.order_service_group=default
#If you use a registry, you can ignore it
service.default.grouplist=127.0.0.1:8091
service.disableGlobalTransaction=false

client.metadataMaxAgeMs=30000
#Transaction rule configuration, only for the client
client.rm.asyncCommitBufferLimit=10000
client.rm.lock.retryInterval=10
client.rm.lock.retryTimes=30
client.rm.lock.retryPolicyBranchRollbackOnConflict=true
client.rm.reportRetryCount=5
client.rm.tableMetaCheckEnable=true
client.rm.tableMetaCheckerInterval=60000
client.rm.sqlParserType=druid
client.rm.reportSuccessEnable=false
client.rm.sagaBranchRegisterEnable=false
client.rm.sagaJsonParser=fastjson
client.rm.tccActionInterceptorOrder=-2147482648
client.tm.commitRetryCount=5
client.tm.rollbackRetryCount=5
client.tm.defaultGlobalTransactionTimeout=60000
client.tm.degradeCheck=false
client.tm.degradeCheckAllowTimes=10
client.tm.degradeCheckPeriod=2000
client.tm.interceptorOrder=-2147482648
client.undo.dataValidation=true
client.undo.logSerialization=jackson
client.undo.onlyCareUpdateColumns=true
server.undo.logSaveDays=7
server.undo.logDeletePeriod=86400000
client.undo.logTable=undo_log
client.undo.compress.enable=true
client.undo.compress.type=zip
client.undo.compress.threshold=64k
#For TCC transaction mode
tcc.fence.logTableName=tcc_fence_log
tcc.fence.cleanPeriod=1h
# You can choose from the following options: fastjson, jackson, gson
tcc.contextJsonParserType=fastjson

#Log rule configuration, for client and server
log.exceptionRate=100

#Transaction storage configuration, only for the server. The file, db, and redis configuration values are optional.
store.mode=file
store.lock.mode=file
store.session.mode=file
#Used for password encryption
store.publicKey=

#If `store.mode,store.lock.mode,store.session.mode` are not equal to `file`, you can remove the configuration block.
store.file.dir=file_store/data
store.file.maxBranchSessionSize=16384
store.file.maxGlobalSessionSize=512
store.file.fileWriteBufferCacheSize=16384
store.file.flushDiskMode=async
store.file.sessionReloadReadSize=100

#These configurations are required if the `store mode` is `db`. If `store.mode,store.lock.mode,store.session.mode` are not equal to `db`, you can remove the configuration block.
store.db.datasource=druid
store.db.dbType=mysql
store.db.driverClassName=com.mysql.jdbc.Driver
# 数据库相关需要修改
store.db.url=jdbc:mysql://localhost:3306/seata?useUnicode=true&rewriteBatchedStatements=true
store.db.user=seata
store.db.password=seata
store.db.minConn=5
store.db.maxConn=30
store.db.globalTable=global_table
store.db.branchTable=branch_table
store.db.distributedLockTable=distributed_lock
store.db.vgroupTable=vgroup-table
store.db.queryLimit=100
store.db.lockTable=lock_table
store.db.maxWait=5000

#These configurations are required if the `store mode` is `redis`. If `store.mode,store.lock.mode,store.session.mode` are not equal to `redis`, you can remove the configuration block.
store.redis.mode=single
store.redis.type=pipeline
store.redis.single.host=127.0.0.1
store.redis.single.port=6379
store.redis.sentinel.masterName=
store.redis.sentinel.sentinelHosts=
store.redis.sentinel.sentinelPassword=
store.redis.maxConn=10
store.redis.minConn=1
store.redis.maxTotal=100
store.redis.database=0
store.redis.password=
store.redis.queryLimit=100

#Transaction rule configuration, only for the server
server.recovery.committingRetryPeriod=1000
server.recovery.asynCommittingRetryPeriod=1000
server.recovery.rollbackingRetryPeriod=1000
server.recovery.timeoutRetryPeriod=1000
server.maxCommitRetryTimeout=-1
server.maxRollbackRetryTimeout=-1
server.rollbackRetryTimeoutUnlockEnable=false
server.distributedLockExpireTime=10000
server.session.branchAsyncQueueSize=5000
server.session.enableBranchAsyncRemove=false
server.enableParallelRequestHandle=true
server.enableParallelHandleBranch=false
server.applicationDataLimit=64000
server.applicationDataLimitCheck=false

server.raft.server-addr=127.0.0.1:7091,127.0.0.1:7092,127.0.0.1:7093
server.raft.snapshotInterval=600
server.raft.applyBatch=32
server.raft.maxAppendBufferSize=262144
server.raft.maxReplicatorInflightMsgs=256
server.raft.disruptorBufferSize=16384
server.raft.electionTimeoutMs=2000
server.raft.reporterEnabled=false
server.raft.reporterInitialDelay=60
server.raft.serialization=jackson
server.raft.compressor=none
server.raft.sync=true



#Metrics configuration, only for the server
metrics.enabled=true
metrics.registryType=compact
metrics.exporterList=prometheus
metrics.exporterPrometheusPort=9898

```

此配置文件的数据库是 seata-server 回滚事务支持的数据库，相关的 sql 文件在 `apache-seata-2.2.0-incubating-bin\seata-server\script\server\db`

> 目前，所有测试环境，如 nacos, seata-server 都是本地服务，所以部分配置可能需要根据实际运行情况进行更改；
> 例如， 所有更 8848 端口相关的地址，多半是 nacos 服务地址，需要重新指定IP.

* 特别注意 service.vgroupMapping
  * 此配置文件的 service.vgroupMapping 配置是对应 各自 Spring boot 服务的集群命名
