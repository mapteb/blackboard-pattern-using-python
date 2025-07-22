import concurrent
import time
from bbcomps.KSInterface import KSInterface
from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard

class KSType1(KSInterface):
    def __init__(self, name):
        self.name = name       

    async def process(self, subTask: BBSubTask, bb: Blackboard):
        # complete subTask and update the blackboard
        print(">> KS worker performing subTask in a Coroutine")
        future1 = self.performTask() # asyncio.sleep(2) # print(">> finished subTask") 
        if future1.result():
            print(">> KS completed the subTask and updating the Blackboard: ")
            subTask.taskDef = "bla"
            subTask.isComplete = True 
            bb.updateSubTask(subTask)

    def long_running_task(self, name: str, duration: float):
        """A simulated long-running task."""
        print(f">> Task {name}: Starting...")
        time.sleep(duration)
        print(f">> Task {name}: Finished.")
        return f"Result of {name}"        

    def performTask(self):
        # perform some non-trivial task
        """Submits a task to an executor and returns a Future object."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.long_running_task, "long-running", 2.0)
            return future

