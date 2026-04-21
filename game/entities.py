from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass(frozen=True)
class Question:
    question: str
    options: List[str]
    answer: str

@dataclass(frozen=True)
class GameState:
    current_question: Question
    players_answers: Dict[str, str] = field(default_factory=dict)
    correct_answer: Optional[str] = None
    time_left: int = 10

    def to_dict(self):
        return {
            "question": self.current_question.question,
            "options": self.current_question.options,
            "correct": self.correct_answer,
            "time_left": self.time_left
        }