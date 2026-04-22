import random

class GameLogic:
    def __init__(self):
        self.questions = [
            {
                "pergunta": "Revelado pelo Sporting...",
                "opcoes": ["Cristiano Ronaldo","Raúl","Benzema","Di Stéfano"],
                "correta": "Cristiano Ronaldo"
            },
            {
                "pergunta": "Volante campeão do mundo em 2014...",
                "opcoes": ["Kroos","Lahm","Goretzka","Schweinsteiger"],
                "correta": "Schweinsteiger"
            },
            {
                "pergunta": "Único jogador a vencer Champions...",
                "opcoes": ["Rijkaard","Gattuso","Seedorf","Pirlo"],
                "correta": "Seedorf"
            },
            {
                "pergunta": "Maior artilheiro da Copa...",
                "opcoes": ["Müller","Klose","Podolski","Gomez"],
                "correta": "Klose"
            },
            {
                "pergunta": "Zagueiro ídolo do Milan...",
                "opcoes": ["Maldini","Nesta","Baresi","Cannavaro"],
                "correta": "Maldini"
            },
            {
                "pergunta": "Francês Bola de Ouro 98...",
                "opcoes": ["Henry","Platini","Mbappé","Zidane"],
                "correta": "Zidane"
            },
            {
                "pergunta": "Cérebro do Barcelona...",
                "opcoes": ["Iniesta","Busquets","Xavi","Fabregas"],
                "correta": "Xavi"
            },
            {
                "pergunta": "Brasileiro do Santos...",
                "opcoes": ["Neymar","Robinho","Ganso","Rodrygo"],
                "correta": "Neymar"
            },
            {
                "pergunta": "Sueco personalidade forte...",
                "opcoes": ["Larsson","Ibrahimovic","Bergkamp","Shevchenko"],
                "correta": "Ibrahimovic"
            },
            {
                "pergunta": "Lateral com mais títulos...",
                "opcoes": ["Cafu","Marcelo","Maicon","Daniel Alves"],
                "correta": "Daniel Alves"
            }
        ]

        random.shuffle(self.questions)
        self.index = 0

    def next_question(self):
        if self.index >= len(self.questions):
            return None

        q = self.questions[self.index]
        self.index += 1

        opcoes = list(q["opcoes"])
        random.shuffle(opcoes)

        return {
            "pergunta": q["pergunta"],
            "opcoes": opcoes,
            "correta": q["correta"]
        }

    def check_answer(self, answer):
        return answer == self.questions[self.index - 1]["correta"]