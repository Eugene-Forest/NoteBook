# 用来存储从惠州学院新闻网获取的一个新闻对象

class HzuNews:
    """一个简单的新闻信息数据结构"""

    def __init__(self, title, link, time):
        self.title = title
        self.link = link
        self.time = time

    def get_title(self):
        return self.title
