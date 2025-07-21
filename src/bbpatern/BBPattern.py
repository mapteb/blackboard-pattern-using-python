

import asyncio
from dataclasses import dataclass
import threading
from typing import List
import concurrent.futures
import time

@dataclass
class BBSubTask:
    id: str
    taskDef: str
    isComplete: bool


@dataclass
class BBTask:
    subTasks: List[BBSubTask]

    def isCompleted(self) -> bool:
        return next(x for x in self.subTasks if x)

class BlackBoard:
    _state: BBTask
    list_lock = threading.Lock()

    def __init__(self):
        self._observers = []
        self._state = BBTask([])

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, bbSubTask: BBSubTask):
        for observer in self._observers:
            if not bbSubTask.isComplete:
                observer.update(bbSubTask)

    def updateSubTask(self, bbSubTask: BBSubTask):
        # if the isComplete is False add this subTask as a new task
        if not bbSubTask.isComplete:
            self.addSubTask(bbSubTask)
        else:    
            # multiple KSs could be calling thi
            # so update the list concurrently
            with self.list_lock:  # Acquire lock
                sts: List[BBSubTask] = []
                for bbt in self.state.subTasks:
                    if bbt.id == bbSubTask.id:
                        sts.append(bbSubTask)
                    else:
                        sts.append(bbt) 

                self._state.subTasks = sts                      

    def addSubTask(self, bbSubTask: BBSubTask):
        self._state.subTasks.append(bbSubTask)
        self.notify(bbSubTask)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        print(">> appending subTasks")
        self._state = state
        self.notify()


class KS:
    def __init__(self, name, bb: BlackBoard):
        self.name = name
        self.bb = bb

    async def process(self, subTask: BBSubTask):
        # complete subTask and update the blackboard
        print(">> KS worker performing subTask in a Coroutine")
        future1 = self.performTask() # asyncio.sleep(2) # print(">> finished subTask") 
        if future1.result():
            print(">> KS completed the subTask and updating the Blackboard: ")
            subTask.taskDef = "bla"
            subTask.isComplete = True 
            self.bb.updateSubTask(subTask)

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
        
        
        
class BBController:
    def __init__(self, name, bb: BlackBoard):
        self._name = name
        self._bb = bb
        self.kslist: List[KS] = []       

    def update(self, bbSubTask: BBSubTask):
        print(">> BBController received a new subTask")
        # find elig KS and launch the KS as a coroutine
        print(">> BBController assigning the subTask to a KS worker")
        ks = KS("ks-1", self._bb)
        # self.launchKSWorker(ks, bbSubTask)
        asyncio.run(ks.process(bbSubTask))

    def launchKSWorker(self, ks: KS, bbSubTask: BBSubTask):
        # loop = asyncio.new_event_loop()  # Create a new event loop
        # asyncio.set_event_loop(loop)         
        # fire and forget
        print(">> launching KS")
           
        
def main():
    bb = BlackBoard()
    bbController = BBController("A", bb)

    bb.subscribe(bbController)

    # add subtasks when they arrive (possibly n a stream)
    print(">> adding a new subTask to he Blackboard")
    bbSubTask = BBSubTask("id1", "subTask1", False)
    bb.addSubTask(bbSubTask)

if __name__ == "__main__":
    main()