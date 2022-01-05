# get some information from school's website
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

from src.instance.HzuNews import HzuNews

# 定义常量惠州学院新闻网 https://news.hzu.edu.cn
HZU_NEWS_LINK = "https://news.hzu.edu.cn"


def get_news_from_hzu():
    """
    获取惠州学院的新闻信息集合。

    :return: 一个包含链接和文字的新闻列表。
        若为空，说明该方法需要更新。
    """
    try:
        html = urlopen(HZU_NEWS_LINK)
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
        # 获取新闻链接以及文本
        items = bs.find('div', {'class': {'post-body'}}) \
            .find('ul', {'class': {'post-news'}}) \
            .findAll('li', {'class': {'xxyw-news-item'}})
        news_list = []
        for item in items:
            time = item.find('div', {'class': 'xxye-time'}).get_text()
            title = item.a['title']
            link = item.a['href']
            # 判断新闻链接是否完整，如果不完整则补充前缀
            if "http" not in link:
                link = HZU_NEWS_LINK + link
            news_list.append(HzuNews(title, link, time))
        return news_list
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None


def get_news_title():
    """
    用来测试网页结构是否更改或验证更改程度。

    :return: 当返回为假，说明网站发生变动；
        若返回为真，说明在title之前的Html结构没有变动或没有影响。
    """
    try:
        html = urlopen("https://news.hzu.edu.cn/")
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return False
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return False
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取区块标题
        title = bs.find('h3', {'class': {'post-title'}})
        print("title is: " + title.get_text())
        return True
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return False


def get_item_link_content():
    try:
        html = urlopen("https://news.hzu.edu.cn/2021/0308/c9430a205755/page.htm")
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
        # 获取新闻链接以及文本
        items = bs.find('div', {'class': 'wp_articlecontent'})\
            .find_all('p',{'style': {'text-indent:2em;text-align:left;'}})
        for item in items:
            print(item.get_text())
        return items
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None


# test code
if __name__ == '__main__':
    newsList = get_news_from_hzu()
    for news in newsList:
        print(news.title)
        print(news.time)
        print(news.link)
    get_item_link_content()
