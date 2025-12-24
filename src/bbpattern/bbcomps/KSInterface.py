from abc import ABC, abstractmethod
from typing import Dict

from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard


class KSInterface(ABC):
            
    @abstractmethod
    def process(self, bb_sub_task: BBSubTask, bb: Blackboard):
        pass