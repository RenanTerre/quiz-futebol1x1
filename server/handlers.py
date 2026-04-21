import json
import uuid
import tornado.web
import tornado.websocket
from game.logic import GameLogic

rooms = {}

class CreateRoomHandler(tornado.web.RequestHandler):
    def get(self):
        room_id = str(uuid.uuid4())[:6]
        rooms[room_id] = GameLogic()

        self.write({
            "room_id": room_id,
            "link": f"http://localhost:8888/?sala={room_id}"
        })


class GameWebSocket(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        self.room_id = self.get_argument("sala", None)

        if not self.room_id or self.room_id not in rooms:
            self.close()
            return

        self.game = rooms[self.room_id]

    def on_message(self, message):
        data = json.loads(message)
        action = data.get("action")

        if action == "next":
            q = self.game.next_question()

            if not q:
                self.write_message(json.dumps({
                    "type": "game_over",
                    "result": self.game.get_result()
                }))
                return

            self.write_message(json.dumps({
                "type": "update",
                "state": {
                    "question": q["pergunta"],
                    "options": q["opcoes"],
                    "correct": q["correta"]
                }
            }))

        elif action == "answer":
            answer = data.get("answer")
            correct = self.game.check_answer(answer)

            self.write_message(json.dumps({
                "type": "answer_result",
                "correct": correct
            }))