# final

## final 类

如果在类的声明中添加final修饰，那么表示该类无法扩展即 **无法创建final类的子类**。

由于无法继承final的类，那么也就无法重写该类声明的方法。



## final 方法

如果为类声明的方法添加final修饰，则表示该方法不会被子类的方法重写。如果在静态方法中的声明中添加final修饰，那么该方法就不会被子类的方法隐藏（hide）。

:::{note}
关于类方法重写与隐藏，参见java类的继承与多态。
:::



## final 字段

**final修饰的字段只能被赋值一次**。从创建线程安全的示例的角度来看，将只赋值一次的字段声明为final也是十分重要的。

对普通final字段的赋值有以下两种：

```java
//way 1: 声明时赋值
class Something{
   final int value=123;
}

//way 2: 构造函数中赋值
class Something{
   final int value;
   Something(){
      this.value=123;
   }
}
```

对final静态字段的赋值有以下两种：

```java
//way 1: 声明时赋值
class Something{
   static final int value=123;
}

//way 2: 静态初始代码块中赋值
class Something{
   static final int value;

   static{
      value=123;
   }
}
```

:::{note}
将方法中的参数声明为final。在一某些情况下，传入方法的参数的值是不会变的，那么将其声明为final的话可以保证在该方法内不会由于操作失误而导致参数值的改变。

```java
public void PrintMessage(final String message){ ... }
```
:::
