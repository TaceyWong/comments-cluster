# coding:utf-8

import re
from base import CommentSource
from utils.net import FetchTool


class NetEaseSource(CommentSource):
    name = u"网易"
    site = "163.com"
    docid_re = re.compile(r"([a-zA-Z0-9]{16})\.html")
    comment_temp = "http://comment.api.163.com/" \
                   "api/v1/products/a2869674571f77b5a0867c3d71db5856/" \
                   "threads/{}/app/comments/newList?" \
                   "offset=0&limit=40"

    @classmethod
    def parse_search_result(cls, content):
        result = cls.docid_re.findall(content)
        return result

    @classmethod
    def get_comments(cls, search_result):
        for item in search_result:
            url = cls.comment_temp.format(item)
            print url
            content = FetchTool.get_json(url)
            print content
