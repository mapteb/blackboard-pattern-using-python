## Blackboard Design Pattern Using Python

This repo has an implementation of the [Blackboard design pattern](https://en.wikipedia.org/wiki/Blackboard_(design_pattern)) in Python

### Components

The module bbpattern has three classes - Blackboard, BBController and KS (KnowledgeSource possibly using AI Agent). The Blackboard object holds a BBTask object which inturn holds a List[BBSubTask] object. The BBController holds a set of KS objects. The KS object has an asynchronous process() method. Each KS (possibly using an AI Agent) is specialized in solving a specific problem.

### How it Works

The Blackboard Pattern solves (or partially solves) a large complex problem by assembling part solutions.
The blackboard engine (the main() method) receives data (possibly as a data stream from various IoT devices) that need to be analyzed and some action taken (like an autonomous vehicle that needs to take the next step).

1. The engine adds the BBController as a subscriber (Observer) to the Blackboard. It also configues the controller with a set of KS objects.
2. The engine places each sub-task that it receives from an external source on the Blackboard. 
3. The Blackboard updates the BBController whenever its state changes (subTask is addded)
4. The BBController holds a set of KS objects that it can launch as a worker Coroutine by assigning the subTask. Each KS object is specialized in handling a a part of the whole problem. The BBController launches the KS that is knowledgable in handling a specfic subTask.
5. The KS worker/s perform the subTask asynchronously. When completed, updates the Blackboard with the completed subTask.
6. A BBTask is considered completed when all the BBSubTasks have their isComplete() returning True.

### Usage
```
git clone https://github.com/mapteb/blackboard-pattern-using-python.git

When the app is run  using - python src\bbpattern\BBPatternApp.py, the following output is generated:

>> adding a new sub_task to the Blackboard
>> BBController received a new sub_task
>> BBController assigning the sub_task to a KS worker
>> KS worker ks-type1 performing sub_task taskType1
>> adding a new sub_task to the Blackboard
>> KS ks-type1 completed the sub_task taskType1
>> BBController received a new sub_task
>> BBController assigning the sub_task to a KS worker
>> BBController updating the Blackboard with the completed sub_task taskType1
>> KS worker ks-type2 performing sub_task taskType2
>> KS ks-type2 completed the sub_task taskType2
>> BBController updating the Blackboard with the completed sub_task taskType2
```

### Use Cases

Here are some scenarios where the Blackbord pattern could be employed

1. Stream of sensors data in an autonomous vehicle and the vehicle needs to take the next set of acions incrementally
2. A TV station headquarters receiving stream of election voting counts from various sub-stations and need to create a dashboard of the results incrementally (The KS workers for various regions like Northeast, South, etc. have specialized knowledge of how to analyze the election counts of their regions)
etc.
