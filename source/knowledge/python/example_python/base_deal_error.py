# 可靠的网络连接以及异常处理
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.head.title
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None
    return title


if __name__ == '__main__':
    title = getTitle('https://www.hzu.edu.cn/')
    if title is None:
        print("Title could not be found!")
    else:
        print(title)
