# coding:utf-8

from .base import CommentSource


class BaiJiaHandler(CommentSource):
    name = u"百度百家"
    site = "baidu.com"

    @classmethod
    def parse_search_result(cls, content):
        pass

    @classmethod
    def get_comments(cls, search_result):
        "https://mbd.baidu.com/po/api/comment/getInfo.jsonp?ver=3.0&tid=n%20ews_14648952402780430079&comType=feednews&nid=news_14648952402780430079"
