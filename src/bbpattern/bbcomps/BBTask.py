from dataclasses import dataclass
from typing import List

from bbcomps.BBSubTask import BBSubTask

@dataclass
class BBTask:
    subTasks: List[BBSubTask] # type: ignore

    def isCompleted(self) -> bool:
        return next(x for x in self.subTasks if x)