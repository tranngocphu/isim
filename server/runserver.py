import webbrowser
from tornado import web, options, ioloop

from config import STATIC_ROOT, TEMPLATE_ROOT, SERVER_PORT
from server.views import HomeView



def make_app():        
    # output all events to the terminal
    options.parse_command_line() 
    return web.Application([   
            (r"/", HomeView),            
        ],
        debug=True,
        template_path=TEMPLATE_ROOT,
        static_path=STATIC_ROOT,
        static_url_prefix="/static/",
    )        



if __name__ == "__main__":
    url = "http://127.0.0.1:{}/".format(SERVER_PORT)
    app = make_app()
    app.listen(SERVER_PORT)
    print("\nThe app is served at {}".format(url))
    webbrowser.open(url, new=2)
    ioloop.IOLoop.current().start()   