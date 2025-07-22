from abc import ABC, abstractmethod
from typing import Dict

from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard


class KSInterface(ABC):

    # def __init__(self, name):
    #     super.__init__(self)
    #     self._name = name
            
    @abstractmethod
    def process(self, bbsubTask: BBSubTask, bb: Blackboard):
        pass