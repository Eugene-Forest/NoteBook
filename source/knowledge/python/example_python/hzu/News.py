import string


class News:
    """
    一个新闻对象，存储新闻标题信息以及具体内容，并存储外链图片；当新闻链接为空字符串时，
    该新闻对象是一个存有文章；当新闻链接不为空时，该新闻对象是一个外链新闻。
    """

    """文章段落文本组"""
    paragraphs = []

    """外链图片信息组"""
    images = []

    """新闻详细介绍链接"""
    pageLink = ""

    """新闻标题"""
    title = ""

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def push_paragraph(self, paragraph: string):
        self.paragraphs.append(paragraph)

    def pop_paragraph(self):
        return self.paragraphs.pop()

    def push_image(self, image: Image):
        self.images.append(image)

    def pop_image(self):
        return self.images.pop()

    def get_link(self):
        return self.pageLink

    def set_link(self, link):
        self.pageLink = link

    def set_paragraphs(self, paragraphs):
        self.paragraphs = paragraphs[:]

    def set_images(self, images):
        self.images = images[:]

    def get_images(self):
        return self.images[:]

    def get_paragraphs(self):
        return self.paragraphs[:]

    def print_news_content(self):
        print("Title :" + self.title)
        print("Hyperlink : "+self.pageLink)
        print("Here is article".center(30, '-'))
        for paragraph in self.paragraphs:
            print(paragraph)
        print("".center(30, '-'))
        print("images len is "+str(len(self.images)))
        for image in self.images:
            print(image.get_title() + ":" + image.get_link())
