from dataclasses import dataclass
from typing import List

from bbcomps.BBSubTask import BBSubTask

@dataclass
class BBTask:
    sub_tasks: List[BBSubTask] # type: ignore

    def is_completed(self) -> bool:
        return next(x for x in self.sub_tasks if x)