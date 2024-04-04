from dataclasses import dataclass
from typing import List

@dataclass
class Classifier:
    id: str
    name: str
    description: str
    type: str
    size: int
    format: str
    accuracy: float
    status: str
    rating: int
    path: str
    isPublic: bool
    owners: List[str]
