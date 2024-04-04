from dataclasses import dataclass
from typing import List

@dataclass
class EventPayload:
    id: str
    name: str
    description: str
    type: str
    format: str
    status: str
    path: str
    isPublic: bool
    owners: List[str]
    
