from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from server.handlers import CreateRoomHandler, GameWebSocket
import os

BASE_DIR = os.path.dirname(__file__)

app = Application([
    (r"/api/create-room", CreateRoomHandler),
    (r"/ws", GameWebSocket),
    (r"/(.*)", StaticFileHandler, {
        "path": os.path.join(BASE_DIR, "client", "static"),
        "default_filename": "index.html"
    }),
])

if __name__ == "__main__":
    app.listen(8888)
    print(" Rodando em http://localhost:8888")
    IOLoop.current().start()