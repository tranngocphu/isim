import tornado.ioloop

from server.handlers import TestHandler


def make_app():
    return tornado.web.Application([
        (r"/", TestHandler)
    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()