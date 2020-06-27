from tornado.web import RequestHandler



class TestHandler(RequestHandler):
    def get(self):
        self.write("Hello, test!")