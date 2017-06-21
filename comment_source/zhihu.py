# coding:utf-8


import re
from base import CommentSource
from utils.net import FetchTool


class ZhiHuHandler(CommentSource):
    name = u"知乎"
    site = "zhihu.com"
    url_re = re.compile(r'question\\/(\d+)\\/answer', re.S)

    def parse_search_result(self, content):
        result = self.url_re.findall(content)
        return result

    def get_comments(self, search_result):
        # 需要模拟登陆
        comments_url = "https://www.zhihu.com/api/v4/questions/{}/answers?&offset=0&limit=100&sort_by=default"
        for item in search_result:
            url = comments_url.format(item)
            print url
            content = FetchTool.get_json(url)
            print content
