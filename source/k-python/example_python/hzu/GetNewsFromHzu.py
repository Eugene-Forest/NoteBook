# get some information from school's website
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 定义常量惠州学院新闻网 https://news.hzu.edu.cn
HZU_NEWS_LINK = "https://news.hzu.edu.cn"


def get_news_from_hzu():
    """
    获取惠州学院新闻网的学校要闻的新闻信息集合。

    :return: 一个包含链接和文字的新闻列表。
        若为空，说明该方法需要更新。
    """
    try:
        html = urlopen(HZU_NEWS_LINK)
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻链接以及文本
        items = bs.find('div', {'class': {'post-body'}}) \
            .find('ul', {'class': {'post-news'}}) \
            .findAll('li', {'class': {'xxyw-news-item'}})
        news_list = []
        for item in items:
            title = item.a['title']
            link = item.a['href']
            news = News(title)
            # 判断新闻链接是否完整，如果不完整则补充前缀
            if "http" not in link:
                news = __get_news_link_content(news, HZU_NEWS_LINK + link)
            else:
                news.set_link(link)
            news_list.append(news)
        return news_list
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return None
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return None


def __get_news_link_content(news: News, article_url):
    try:
        html = urlopen(article_url)
        print("open sub url")
    except HTTPError as e:
        print(e)
        print('The page is not exist or have a error in getting page.')
        return news
    except URLError as e:
        print(e)
        print("url is wrong or the url couldn't open.")
        return news
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # 获取新闻文章主体
        article = bs.find('div', {'class': 'wp_articlecontent'})
        images = []
        paragraphs = []
        # 找到主体文本
        for item in article.find_all(style='text-indent:2em;text-align:left;'):
            paragraphs.append(item.get_text())
        for item in article.find_all('img', {'data-layer': "photo"}):
            link = item['src']
            if "http" not in link:
                link = HZU_NEWS_LINK + link
            # 获取图片的题注，其位置一般在 img 父标签的下一个兄弟标签
            title = item.parent.next_sibling.get_text()
            images.append(Image(title, link))
        news.set_paragraphs(paragraphs)
        news.set_images(images)
        return news
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return news


if __name__ == '__main__':
    for element in get_news_from_hzu():
        print(element.print_news_content())
