import sys
import os

sys.path.append(os.path.dirname(__file__))

from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from server.handlers import CreateRoomHandler, GameWebSocket

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
    PORT = 8888  # pode trocar se quiser
    app.listen(PORT)
    print(f" Rodando em http://localhost:{PORT}")
    IOLoop.current().start()