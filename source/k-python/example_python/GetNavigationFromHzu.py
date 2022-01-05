# get information from hzu navigation

from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_menu_from_hzu_navigation():
    """
    获取惠州学院官网的导航栏的 HTML 文本。

    :return: 一个 ul 标签文本
    """

    try:
        html = urlopen("https://www.hzu.edu.cn/")
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
        return bs.find(id='naver').find('ul', {'class': {'wp-menu'}})
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None


def print_children_from_menu(content):
    for element in content.children:
        print(element)


def print_descendants_from_menu(content):
    for element in content.descendants:
        print(element)


if __name__ == '__main__':
    menu = get_menu_from_hzu_navigation()
    print_children_from_menu(menu)
    print(''.center(20, '*'))
    print_descendants_from_menu(menu)
