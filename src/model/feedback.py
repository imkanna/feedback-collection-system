from dataclasses import dataclass

@dataclass
class Feedback:
    id: str
    reference: str
    name: str
    message: str
    created: float