# 事务

[扩展](https://javaguide.cn/system-design/framework/spring/spring-transaction.html#%E4%BA%8B%E5%8A%A1%E5%B1%9E%E6%80%A7%E8%AF%A6%E8%A7%A3)

在应用程序中，事务管理是确保数据的一致性和完整性的重要组成部分。Spring 事务管理提供了一种可靠且灵活的方式来管理事务，确保在数据库操作过程中的 ***原子性、一致性、隔离性和持久性***。

## 事务的特性 ACID

Spring 事务管理的目标是确保在应用程序中的数据库操作过程中，能够实现以下目标：

* 原子性（Atomicity）：事务中的所有操作要么全部成功执行并提交，要么全部失败并回滚，确保数据库的一致性。
* 一致性（Consistency）：事务的执行过程中，数据库从一个一致的状态转变为另一个一致的状态，不会破坏数据的完整性。
* 隔离性（Isolation）：多个并发事务之间应该相互隔离，每个事务的操作应该看起来像是在独立执行，避免数据冲突和不一致性。
* 持久性（Durability）：一旦事务提交，其对数据库的修改应该是永久性的，即使在系统故障或重启后也能够恢复。

> Atomicity, isolation, and durability are properties of the database, whereas consis‐ tency (in the ACID sense) is a property of the application. The application may rely on the database’s atomicity and isolation properties in order to achieve consistency, but it’s not up to the database alone.
> 翻译过来的意思是：原子性，隔离性和持久性是数据库的属性，而一致性（在 ACID 意义上）是应用程序的属性。应用可能依赖数据库的原子性和隔离属性来实现一致性，但这并不仅取决于数据库。因此，字母 C 不属于 ACID 。

***只有保证了事务的持久性、原子性、隔离性之后，一致性才能得到保障。也就是说 A、I、D 是手段，C 是目的！***

## 事务定义

在 Spring 中，事务定义（Transaction Definition）用于定义事务的属性，如隔离级别、传播行为、超时设置等。事务定义可以通过编程方式或声明式方式来定义。

编程式事务定义是通过编写代码来显式地管理事务的开始、提交和回滚。你可以使用编程式事务管理的 API（如 TransactionTemplate）来定义事务的属性。

声明式事务定义是通过在方法或类级别上使用注解或 XML 配置来定义事务的属性。Spring 提供了 @Transactional 注解，用于在方法级别上定义事务的属性。你可以在需要进行事务管理的方法上添加 @Transactional 注解，并指定事务的属性。

事务的属性

* 传播行为（Propagation）
* 隔离级别（Isolation）
* 只读标志（ReadOnly）
* 超时设置（Timeout）
* 等。

通过定义适当的事务属性，你可以控制事务的行为和特性。

### Spring 声明式事务处理 - `@Transactional`

通常，在三层分层架构中，web 层有 controller，业务逻辑层有 service，数据访问层有 repository。

一般来说，“事务单元” 以 service 方法为模型，并被视为 “事务边界”。

我们可以在 Service 层方法上添加 Spring 的 @Transactional 注解来定义事务范围。该方法中的所有数据库操作都将在一个事务中运行。如果方法执行成功，则事务将被提交。如果在方法执行过程中出现任何 RuntimeException 异常，则事务将被回滚。

我们可以在方法级别添加 @Transactional 注解，使该特定方法具有事务性；也可以在类级别添加 @Transactional 注解，使该类中的所有 public 方法都具有事务性。

添加 @Transactional 注解时，默认情况下：

* 传播（propagation）设置为 REQUIRED，即参与当前事务（如果存在）或启动新事务。
* 如果方法抛出任何 RuntimeException，则回滚事务。
* 如果方法抛出任何受检异常（非 runtime 异常），则不会回滚事务。

可以通过如下方式指定 @Transactional 属性来自定义这种行为：

```java

@Service
class UserService {
    private final JdbcTemplate jdbcTemplate;
    
    @Transactional(
            propagation = Propagation.REQUIRES_NEW,
            rollbackFor = DuplicateUserException.class,
            noRollbackFor = IllegalArgumentException.class)
    void register(User user) throws DuplicateUserException {
        String sql = "...";
        jdbcTemplate.update(sql);
    }
}

class DuplicateUserException extends Exception {}
```

在上面的代码片段中，我们将传播级别指定为 REQUIRES_NEW，而不是默认的 REQUIRED。REQUIRES_NEW 传播级别会暂停当前事务（如果存在），启动一个新事务，执行数据库操作，提交事务，然后恢复先前暂停的事务。

此外，我们还指定了如果出现 DuplicateUserException，即使它是一个受检异常，也要回滚事务。以及，如果出现 IllegalArgumentException（即使它是一个 RuntimeException），也不回滚事务。

@Transactional 的常用配置参数总结

|   属性名    |                             说明                             |
| :---------: | :----------------------------------------------------------: |
| propagation |              事务的传播行为，默认值为 REQUIRED               |
|  isolation  |              事务的隔离级别，默认值采用 DEFAULT              |
|  readOnly   |           指定事务是否为只读事务，默认值为 false。           |
| rollbackFor | 用于指定能够触发事务回滚的异常类型，并且可以指定多个异常类型 |
|   timeout   | 事务的超时时间，默认值为-1（不会超时）。如果超过该时间限制但事务还没有完成，则自动回滚事务。 |

* 超时属性：你可以使用timeout属性来定义事务的超时时间，单位为秒。如果事务在规定时间内未完成，它将被自动回滚。例如：@Transactional(timeout = 30)表示事务的超时时间为30秒。
* 只读属性：通过设置readOnly属性为true，可以告诉Spring该事务只读，不会修改数据。这可以提高事务的性能。例如：@Transactional(readOnly = true)。
* 回滚条件：你可以使用rollbackFor和noRollbackFor属性来定义在何种异常情况下事务应该回滚或不回滚。默认是运行错误会导致回滚。

## 事务管理器

在 Spring 中，事务管理器（Transaction Manager）是用于管理事务的关键组件。事务管理器负责事务的开始、提交和回滚操作，并与底层的数据库或持久化框架进行交互。

Spring 提供了多种事务管理器的实现，包括：

* DataSourceTransactionManager：用于管理基于 JDBC 的事务，与 JDBC DataSource 进行交互。
* JpaTransactionManager：用于管理基于 JPA（Java Persistence API）的事务，与 JPA EntityManagerFactory 进行交互。
* HibernateTransactionManager：用于管理基于 Hibernate 的事务，与 Hibernate SessionFactory 进行交互。
* JtaTransactionManager：用于管理分布式事务，与 JTA（Java Transaction API）进行交互。

### Spring 编程式事务定义

事务管理的核心操作只有两个：提交和回滚。前面所谓的传播、嵌套、回滚之类的，都是基于这两个操作。

所以 Spring 将事务管理的核心功能抽象为一个事务管理器（Transaction Manager），基于这个事务管理器核心，可以实现多种事务管理的方式。

这个核心的事务管理器只有三个功能接口：

* 获取事务资源，资源可以是任意的，比如 jdbc connection/hibernate mybatis sessio n之类，然后绑定并存储。
* 提交事务 - 提交指定的事务资源。
* 回滚事务 - 回滚指定的事务资源。

```java

// 事务管理器的基础抽象接口，所有的事务管理器都要实现这三个接口
interface PlatformTransactionManager{
    // 获取事务资源，资源可以是任意的，比如jdbc connection/hibernate mybatis session之类
  TransactionStatus getTransaction(TransactionDefinition definition)
      throws TransactionException;
    
    // 提交事务
    void commit(TransactionStatus status) throws TransactionException;
    
    // 回滚事务
    void rollback(TransactionStatus status) throws TransactionException;
}
```

在获取事务资源时，需要根据这个事务的定义来进行不同的配置：

* 比如配置了使用新事务，那么在获取事务资源时就需要创建一个新的，而不是已有的。
* 比如配置了隔离级别，那么在首次创建资源（Connection）时，就需要给 Connection 设置 propagation。
* 比如配置了只读属性，那么在首次创建资源（Connection）时，就需要给 Connection 设置 readOnly。

我们可以发现，这些行为都是在上文中 `@Transactional` 注解的配置实现的功能。

