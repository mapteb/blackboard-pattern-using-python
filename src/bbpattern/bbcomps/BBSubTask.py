from dataclasses import dataclass


@dataclass
class BBSubTask:
    id: str
    task_def: str
    is_complete: bool
