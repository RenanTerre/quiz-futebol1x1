from hardware.display import LCDManager
from hardware.buzzer import BuzzerManager

class HardwareSystem:
    def __init__(self):
        try:
            self.display = LCDManager()
            self.buzzer = BuzzerManager()
        except:
            # Fallback para simulação no terminal
            self.display = LCDManager(mock=True)
            self.buzzer = BuzzerManager(mock=True)

    def victory_sequence(self):
        self.display.show_message("VOCÊ VENCEU!")
        self.buzzer.victory()

# Mock simples para testes em PC (Caso não tenha os drivers instalados)
if __name__ == "__main__":
    hw = HardwareSystem()
    hw.display.show_message("Teste OK")