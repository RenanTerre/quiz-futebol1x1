import os
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Config:
    PORT: int = 8888
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_PATH: str = os.path.join(BASE_DIR, "client", "static")

config = Config()