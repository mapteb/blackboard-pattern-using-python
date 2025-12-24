import time
from bbcomps.KSInterface import KSInterface
from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard

class KSType2(KSInterface):
    def __init__(self, name):
        self.name = name       

    def process(self, sub_task: BBSubTask) -> BBSubTask:
        # complete sub_task and update the blackboard
        print(">> KS worker " + self.name + " performing sub_task " + sub_task.id)
         # asyncio.sleep(2) # print(">> finished sub_task") 
        print(">> KS " + self.name + " completed the sub_task " + sub_task.id)
        sub_task.is_complete = True 
        return sub_task

    def long_running_task(self, name: str, duration: float):
        """A simulated long-running task."""
        print(f">> Task {name}: Starting...")
        time.sleep(duration)
        print(f">> Task {name}: Finished.")
        return f"Result of {name}"        


