from bbcomps.BBController import BBController
from bbcomps.BBSubTask import BBSubTask
from bbcomps.Blackboard import Blackboard
from bbcomps.KSType1 import KSType1

def main():
    bb = Blackboard()
    ksWorkers = {"taskType1": KSType1("ks-type1")}
    bbController = BBController("A", bb, ksWorkers)

    bb.subscribe(bbController)

    # add subtasks when they arrive (possibly in a stream)
    print(">> adding a new subTask to he Blackboard")
    bbSubTask = BBSubTask("id1", "subTask1", False)
    bb.addSubTask(bbSubTask)

if __name__ == "__main__":
    main()