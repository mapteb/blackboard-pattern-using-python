import asyncio
from typing import Dict

from bbcomps.BBSubTask import BBSubTask
from bbcomps.KSInterface import KSInterface
from bbcomps.Blackboard import Blackboard
from bbcomps.KSType1 import KSType1

class BBController:
    def __init__(self, name, bb: Blackboard, ks_workers: Dict[str, KSInterface]): # type: ignore
        self._name = name
        self._bb = bb
        self.kslist: Dict[str, KSInterface] = ks_workers        # type: ignore

    def update(self, bb_sub_task: BBSubTask):
        print(">> BBController received a new sub_task")

        # find elig KS and launch the KS as a coroutine
        
        print(">> BBController assigning the sub_task to a KS worker")
        ks = self.select_KS(bb_sub_task)
        self.execute_KS(ks, bb_sub_task)        

    def execute_KS(self, ks: KSInterface, bb_sub_task: BBSubTask):       
        # fire and forget
        print(">> launching KS")
        asyncio.run(ks.process(bb_sub_task, self._bb))

    def select_KS(self, bb_sub_task: BBSubTask) -> KSInterface:
        # For this demo we are using a simple label to select a KS.
        # The controller could use more complex logic to select a KS.   
        return self.kslist.get(bb_sub_task.id)
        
