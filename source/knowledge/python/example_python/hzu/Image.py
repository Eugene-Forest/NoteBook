class Image:
    """
    一个网络中的图片的数据对象
    """

    imgLink = ""
    imgTitle = ""

    def __init__(self, title, link):
        self.imgLink = link
        self.imgTitle = title

    def get_link(self):
        return self.imgLink

    def get_title(self):
        return self.imgTitle

    def set_title(self, title):
        self.imgTitle = title

    def set_link(self, link):
        self.imgLink = link
