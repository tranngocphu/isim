from tornado.web import RequestHandler



class HomeView(RequestHandler):
    def get(self):
        self.render("index.html")


class TestView(RequestHandler):
    def get(self):
        self.write("Hello, test!")