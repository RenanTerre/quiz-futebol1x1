import json
import uuid
import tornado.web
import tornado.websocket
from game.logic import GameLogic

rooms = {}

class CreateRoomHandler(tornado.web.RequestHandler):
    def get(self):
        room_id = str(uuid.uuid4())[:6]

        rooms[room_id] = {
            "game": GameLogic(),
            "players": [],
            "scores": {"p1": 0, "p2": 0}
        }

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

        self.room = rooms[self.room_id]
        self.room["players"].append(self)

        self.player_id = f"p{len(self.room['players'])}"

        print(f"Jogador entrou: {self.player_id}")

        self.write_message(json.dumps({
            "type": "player_id",
            "player": self.player_id
        }))

        # espera 2 jogadores
        if len(self.room["players"]) < 2:
            self.write_message(json.dumps({"type": "waiting"}))
            return

        self.start_game()

    def start_game(self):
        q = self.room["game"].next_question()

        self.broadcast({
            "type": "start",
            "state": {
                "question": q["pergunta"],
                "options": q["opcoes"],
                "correct": q["correta"]
            }
        })

    def broadcast(self, data):
        for p in self.room["players"]:
            p.write_message(json.dumps(data))

    def on_message(self, message):
        data = json.loads(message)
        action = data.get("action")

        game = self.room["game"]

        if action == "answer":
            answer = data.get("answer")
            correct = game.check_answer(answer)

            if correct:
                self.room["scores"][self.player_id] += 1

            self.broadcast({
                "type": "update_score",
                "scores": self.room["scores"]
            })

            if self.room["scores"][self.player_id] >= 5:
                self.broadcast({
                    "type": "winner",
                    "winner": self.player_id,
                    "scores": self.room["scores"]
                })
                return

            q = game.next_question()

            if not q:
                self.broadcast({
                    "type": "game_over",
                    "scores": self.room["scores"]
                })
                return

            self.broadcast({
                "type": "next_question",
                "state": {
                    "question": q["pergunta"],
                    "options": q["opcoes"],
                    "correct": q["correta"]
                }
            })

    def on_close(self):
        if hasattr(self, "room"):
            if self in self.room["players"]:
                self.room["players"].remove(self)