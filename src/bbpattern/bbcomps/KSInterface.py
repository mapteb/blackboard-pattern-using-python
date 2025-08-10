from abc import ABC, abstractmethod
from typing import Dict

from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard


class KSInterface(ABC):
            
    @abstractmethod
    def process(self, bbsubTask: BBSubTask, bb: Blackboard):
        pass