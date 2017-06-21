# coding:utf-8

import re
import json
from base import CommentSource
from utils.net import FetchTool


class TencentHandler(CommentSource):
    name = u"腾讯"
    site = "qq.com"
    detail_url_re = re.compile('bds\.comm\.iaurl=(.*?);')
    cmt_id_re = re.compile('cmt_id = (\d+);')
    cmt_temp = "http://coral.qq.com/article/{}/comment?commentid=0&reqnum=100"

    @classmethod
    def parse_search_result(cls, content):
        result = cls.detail_url_re.findall(content)
        try:
            result = filter(lambda x: ".htm" in x, json.loads(result[0]))
        except Exception as e:
            print e
            result = []
        return result

    @classmethod
    def get_comments(cls, search_result):
        for item in search_result:
            html = FetchTool.get_content(item)
            cmt_id = cls.cmt_id_re.findall(html)
            if not cmt_id: continue
            url = cls.cmt_temp.format(cmt_id[0])
            print url
            comment = FetchTool.get_json(url)
            print comment
