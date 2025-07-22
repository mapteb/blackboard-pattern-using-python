import threading
from typing import List
from bbcomps.BBTask import BBTask
from bbcomps.BBSubTask import BBSubTask


class Blackboard:
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
