import concurrent
import time
from bbcomps.KSInterface import KSInterface
from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard

class KSType2(KSInterface):
    def __init__(self, name):
        self.name = name       

    async def process(self, sub_task: BBSubTask, bb: Blackboard):
        # complete sub_task and update the blackboard
        print(">> KS worker " + self.name + " performing sub_task " + sub_task.id + " in a Coroutine")
        future1 = self.perform_task() # asyncio.sleep(2) # print(">> finished sub_task") 
        if future1.result():
            print(">> KS " + self.name + " completed the sub_task " + sub_task.id + " and updating the Blackboard: ")
            sub_task.task_def = "bla"
            sub_task.is_complete = True 
            bb.updateSubTask(sub_task)

    def long_running_task(self, name: str, duration: float):
        """A simulated long-running task."""
        print(f">> Task {name}: Starting...")
        time.sleep(duration)
        print(f">> Task {name}: Finished.")
        return f"Result of {name}"        

    def perform_task(self):
        # perform some non-trivial task
        """Submits a task to an executor and returns a Future object."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.long_running_task, "long-running", 2.0)
            return future

