from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_table_from_w3school():
    """
    从 w3school 中获取一个table标签

    :return: 一个 table 标签
    """

    try:
        html = urlopen("https://www.w3school.com.cn/html/html_tables.asp")
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
        return bs.find('table', {'class': 'dataintable'})
    except AttributeError as e:
        print(e)
        print('某个标签元素不存在 或者url错误(服务器不存在)导致html.read()出错')
        return None


def print_all_brother_tr_from_table(table):
    """
    打印表格的除了第一个 tr 之外的所有 tr 标签

    :param table: 被打印的 table 标签文本
    """

    for tr in table.tr.next_siblings:
        print(tr)
    print(''.center(20, '*'))
    for tr in table.find_all('tr')[-1].previous_siblings:
        print(tr)
    print(''.center(20, '*'))
    print(''.center(20, '-'))
    print(table.find_all('tr')[-1].previous_sibling)
    print(''.center(20, '-'))
    print(table.tr.next_sibling)


if __name__ == '__main__':
    print_all_brother_tr_from_table(get_table_from_w3school())
