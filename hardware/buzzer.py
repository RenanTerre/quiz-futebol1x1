import time
from core.config import config

class BuzzerManager:
    def __init__(self, mock=False):
        self.mock = mock
        self.pin = config.BUZZER.PIN

    def beep(self, duration=0.1):
        print("[BUZZER] Beep curto (Acerto)")
        if not self.mock:
            # Lógica GPIO: HIGH -> sleep -> LOW
            pass

    def error(self):
        print("[BUZZER] Som grave (Erro)")
        if not self.mock:
            pass

    def victory(self):
        print("[BUZZER] Melodia de Vitória!")
        if not self.mock:
            for _ in range(3):
                self.beep(0.2)
                time.sleep(0.1)