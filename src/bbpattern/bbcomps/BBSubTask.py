from dataclasses import dataclass


@dataclass
class BBSubTask:
    id: str
    taskDef: str
    isComplete: bool
