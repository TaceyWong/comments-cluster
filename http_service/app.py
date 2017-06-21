# coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path

from tornado.options import options, define

define("port", default=8080, help="指定运行端口，缺省为8080", type=int)
define("debug", default=0, help="0：正常;1：debug模式", type=int)

username = u"Tacey Wong"


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("code")


class UnlockHandler(BaseHandler):
    def get(self):
        self.render("unlock.html")

    def post(self):
        self.set_secure_cookie("code", self.get_argument("code"))
        self.render("search.html", user=username)


class IndexHandler(BaseHandler):
    def get(self):
        self.redirect("/search")


class SearchHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("search.html", user=username)


class LockHandler(BaseHandler):
    def get(self):
        if self.get_argument("logout", None):
            self.clear_all_cookies()
            self.redirect("/unlock")


class Application(tornado.web.Application):
    def __init__(self, debug):
        handlers = self.urls_setting()
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            xsrf_cookies=True,
            login_url="/unlock",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

    def urls_setting(self):
        urls = list()
        urls.append((r'/', IndexHandler))
        urls.append((r'/search', SearchHandler))
        urls.append((r'/lock', LockHandler))
        urls.append((r'/unlock', UnlockHandler))
        print urls
        return urls


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application(debug=options.debug)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
