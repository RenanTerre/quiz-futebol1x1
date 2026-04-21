from game.logic import GameLogic
import uuid

class RoomManager:
    def __init__(self):
        self.rooms = {}

    def create_room(self):
        room_id = str(uuid.uuid4())[:6]
        self.rooms[room_id] = GameLogic()
        return room_id

    def get_room(self, room_id):
        return self.rooms.get(room_id)