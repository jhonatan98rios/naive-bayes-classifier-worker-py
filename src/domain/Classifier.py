from dataclasses import dataclass
from typing import List
from enum import Enum


@dataclass
class Classifier:
    id: str
    name: str
    description: str
    size: int
    format: str
    accuracy: float
    status: str
    rating: int
    path: str
    isPublic: bool
    owners: List[str]
