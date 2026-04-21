from core.config import config

class LCDManager:
    def __init__(self, mock=False):
        self.mock = mock
        if not self.mock:
            # Aqui entraria a importação da biblioteca RPLCD ou similar
            pass

    def show_message(self, message: str):
        # Garante que a mensagem caiba nos limites do LCD (16x2)
        clean_msg = message[:16]
        print(f"[LCD DISPLAY] {clean_msg}")
        
        if not self.mock:
            # Lógica real para escrever nos pinos RS, EN, etc.
            # lcd.write_string(clean_msg)
            pass