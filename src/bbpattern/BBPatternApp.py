from bbcomps.BBController import BBController
from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard
from bbcomps.KSType1 import KSType1

def main():
    bb = Blackboard()
    ks_workers = {"taskType1": KSType1("ks-type1"), "taskType2": KSType1("ks-type2")}
    bb_controller = BBController("A", bb, ks_workers)

    bb.subscribe(bb_controller)

    # add subtasks when they arrive (possibly in a stream)
    print(">> adding a new sub_task to the Blackboard")
    bb_sub_task = BBSubTask("taskType1", "sub_task1", False)
    bb.add_sub_task(bb_sub_task)

    print(">> adding a new sub_task to the Blackboard")
    bb_sub_task = BBSubTask("taskType2", "sub_task2", False)
    bb.add_sub_task(bb_sub_task)    

if __name__ == "__main__":
    main()