# coding:utf-8

import json
import requests


class FetchTool(object):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"

    @classmethod
    def get_content(cls, url):
        header = {
            "User-Agent": cls.ua
        }
        content = ""
        try:
            req = requests.get(url, headers=header)
            content = req.content
            if "请检查您的输入是否正确" in content:
                print "无任何搜索结果"
                content = ""
        except Exception as e:
            print e
        return content

    @classmethod
    def get_json(cls, url):
        content = cls.get_content(url)
        json_data = None
        try:
            json_data = json.loads(content)
        except Exception as e:
            print e
        return json_data
