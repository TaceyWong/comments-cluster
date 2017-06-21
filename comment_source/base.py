# coding:utf-8

from utils.net import FetchTool


class Comment(object):
    def __int__(self):
        self.ori = ""
        self.content = ""
        self.like = 0
        self.unlike = 0
        self.author = 0
        self.avator = ""


class BaiduClient(object):
    search_url = "http://www.baidu.com/s?ie=utf-8&wd=site:{site} {text}"

    @classmethod
    def search(cls, site, title):
        search_url = cls.search_url.format(site=site,
                                           title=title)
        content = FetchTool.get_content(search_url)
        return content


class CommentSource(object):
    name = ""
    site = ""

    @classmethod
    def search(cls, text):
        content = BaiduClient.search(cls.site, text)
        return content

    @classmethod
    def parse_search_result(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def get_comments(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def format_comments(cls, **kwargs):
        raise NotImplementedError
