import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the index context route")

class HelloWorld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World, fellow pythonistas!")

app = tornado.web.Application([
    (r"/",IndexHandler),
    (r"/helloworld",HelloWorld)
])
app.listen(8080)
tornado.ioloop.IOLoop.current().start()