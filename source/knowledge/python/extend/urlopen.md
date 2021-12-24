# urllib.request

我们在网络上浏览网页的最终目的是为了获取信息。通过浏览器打开一个网站的网页，可以认为是从网站上下载了一个 HTML 文件；而这个 HTML 文件中则包含了我们所需要的信息的数据。

```python
from urllib.request import urlopen
html = urlopen('https://www.hzu.edu.cn/main.htm')
content = html.read()
print(content)
```

这段代码运行后打印出的是一个 HTML 文件的源代码。

urlopen 用来打开并读取一个从网络获取的远程对象，可以读取 HTML 文件、图像文件或其他任何文件流。
