# 网络爬虫模型

目前为止，我们处理的都是单个静态页面，然而在实际运用中，我们常常需要在一个根页面的基础上通过内链进入网站的其他界面以获取更多数据，拥有这种功能的程序可以称之为网络爬虫。

之所以叫网络爬虫，是因为它们可以在 Web 上“爬行”。它们 **本质上是一种递归方式**。

## 一个获取惠州学院新闻网要闻的简单爬虫模型

### 新闻数据结构

```{literalinclude} ../example_python/hzu/Image.py
:language: python
```

```{literalinclude} ../example_python/hzu/News.py
:language: python
```

### 新闻的爬虫模型 [^id6]

```{literalinclude} ../example_python/hzu/GetNewsFromHzu.py
:language: python
```

______________________________________________________________________

[^id6]: 2021年4月30日 测试正常
