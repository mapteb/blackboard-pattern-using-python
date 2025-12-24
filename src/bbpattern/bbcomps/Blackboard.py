import threading
from typing import List
from bbcomps.BBTask import BBTask
from bbcomps.BBSubTask import BBSubTask


class Blackboard:
    _state: BBTask
    list_lock = threading.Lock()
    _instance = None 
    
    def __new__(cls): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
            return cls._instance

    def __init__(self):
        self._observers = []
        self._state = BBTask([])

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, bb_sub_task: BBSubTask):
        for observer in self._observers:
            if not bb_sub_task.is_complete:
                observer.update(bb_sub_task)

    def updateSubTask(self, bb_sub_task: BBSubTask):
        # if the is_complete is False add this sub_task as a new task
        if not bb_sub_task.is_complete:
            self.add_sub_task(bb_sub_task)
        else:    
            # multiple KSs could be calling thi
            # so update the list concurrently
            with self.list_lock:  # Acquire lock
                sts: List[BBSubTask] = []
                for bbt in self.state.sub_tasks:
                    if bbt.id == bb_sub_task.id:
                        sts.append(bb_sub_task)
                    else:
                        sts.append(bbt) 

                self._state.sub_tasks = sts                      

    def add_sub_task(self, bb_sub_task: BBSubTask):
        self._state.sub_tasks.append(bb_sub_task)
        self.notify(bb_sub_task)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        print(">> appending sub_tasks")
        self._state = state
        
