import asyncio
from typing import Dict

from bbcomps.BBSubTask import BBSubTask
from bbcomps.KSInterface import KSInterface
from bbcomps.Blackboard import Blackboard
from bbcomps.KSType1 import KSType1

class BBController:
    def __init__(self, name, bb: Blackboard, ksWorkers: Dict[str, KSInterface]): # type: ignore
        self._name = name
        self._bb = bb
        self.kslist: Dict[str, KSInterface] = ksWorkers        # type: ignore

    def update(self, bbSubTask: BBSubTask):
        print(">> BBController received a new subTask")

        # find elig KS and launch the KS as a coroutine
        
        print(">> BBController assigning the subTask to a KS worker")
        ks = self.selectKS(bbSubTask)
        self.executeKS(ks, bbSubTask)        

    def executeKS(self, ks: KSInterface, bbSubTask: BBSubTask):
        # loop = asyncio.new_event_loop()  # Create a new event loop
        # asyncio.set_event_loop(loop)         
        # fire and forget
        print(">> launching KS")
        asyncio.run(ks.process(bbSubTask, self._bb))

    def selectKS(self, bbSubTask: BBSubTask) -> KSInterface:
        #TODO: logic of selecting a KS for a given subTask
        #  return the selected KS        
        return self.kslist.get("taskType1")
        
