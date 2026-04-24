import random

class GameLogic:
    def __init__(self):
        self.questions = [
            {
                "pergunta": "Revelado pelo Sporting, maior artilheiro da história do Real Madrid e único com 5 Champions League",
                "opcoes": ["Cristiano Ronaldo","Raúl","Benzema","Di Stéfano"],
                "correta": "Cristiano Ronaldo"
            },
            {
                "pergunta": "Volante campeão do mundo em 2014, ídolo do Bayern e famoso pelo gol na final da Champions 2013",
                "opcoes": ["Kroos","Lahm","Goretzka","Schweinsteiger"],
                "correta": "Schweinsteiger"
            },
            {
                "pergunta": "Único jogador a vencer Champions com 3 clubes diferentes como titular (Ajax, Real e Milan)",
                "opcoes": ["Rijkaard","Gattuso","Seedorf","Pirlo"],
                "correta": "Seedorf"
            },
            {
                "pergunta": "Maior artilheiro da história da Copa do Mundo, alemão que jogou Bayern e Lazio",
                "opcoes": ["Müller","Klose","Podolski","Gomez"],
                "correta": "Klose"
            },
            {
                "pergunta": "Zagueiro ídolo do Milan, conhecido como Capitano e um dos maiores defensores da história",
                "opcoes": ["Maldini","Nesta","Baresi","Cannavaro"],
                "correta": "Maldini"
            },
            {
                "pergunta": "Jogador francês que ganhou Bola de Ouro em 1998 e marcou dois gols na final da Copa",
                "opcoes": ["Henry","Platini","Mbappé","Zidane"],
                "correta": "Zidane"
            },
            {
                "pergunta": "Meia espanhol, campeão do mundo em 2010 e conhecido como cérebro do Barcelona",
                "opcoes": ["Iniesta","Busquets","Xavi","Fabregas"],
                "correta": "Xavi"
            },
            {
                "pergunta": "Jogador brasileiro revelado pelo Santos, campeão da Libertadores 2011 e vendido ao Barcelona",
                "opcoes": ["Neymar","Robinho","Ganso","Rodrygo"],
                "correta": "Neymar"
            },
            {
                "pergunta": "Atacante sueco, jogou em mais de 6 grandes clubes europeus e famoso pela personalidade forte",
                "opcoes": ["Larsson","Ibrahimovic","Bergkamp","Shevchenko"],
                "correta": "Ibrahimovic"
            },
            {
                "pergunta": "Lateral brasileiro, mais títulos da história do futebol, jogou no Barcelona e PSG",
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
