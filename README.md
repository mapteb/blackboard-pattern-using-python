## Blackboard Design Pattern Using Python

This repo has an implementationn of the [Blackboard design pattern](https://en.wikipedia.org/wiki/Blackboard_(design_pattern)) in Python

### Components

The module bbpattern has three classes - Blackboard, BBController and KS (KnowledgeSource). The Blackboard object holds a BBTak object which inturn holds a List[BBSubTak] onject. The BBController holds a set of KS objects. The KS object has an asynchronous process() method

### How it Works

The Blackboard Pattern solves (partially solves) a large complex problem by assembling part solutions.
The blackboard engine (the main() method) receives data (possibly as a data stream from various IoT devices) that need to be analyzed and some action taken (like an autonomous vehicle that needs to take the next step).

1. The engine adds the BBController as a subscriber (Observer) to the Blackboard
2. The engine places each sub-task that it receives from an external source on the Blackboard. 
3. The Blackboard updates the BBController whenever its state changes (subTask is addded)
4. The BBController holds a set of KS objects that it can launch as a worker Coroutine by assigning the subTask. Each KS object is specialized in handling a a part of the whole problem. The BBController launches the KS that is knowledgable in handling a specfic subTask.
5. The KS worker/s perform the subTask asynchronously. When completed, updates the Blackboard with the completed subTask.
6. A BBTask is considered completed when all the BBSubTasks have their isComplete() returning True.

### Input / Output

When the module is run (python .\BBPatternApp.py), the following output is generated:

&gt;&gt; adding a new subTask to he Blackboard<br>
&gt;&gt; BBController received a new subTask<br>
&gt;&gt; BBController assigning the subTask to a KS worker<br>
&gt;&gt; KS worker performing subTask in a Coroutine<br>
&gt;&gt; Task long-running: Starting...<br>
&gt;&gt; Task long-running: Finished.<br>
&gt;&gt; KS completed the subTask and updating the Blackboard<br>

### Use Cases

Here are some scenarios where the Blackbord pattern could be employed

1. Stream of sensors data in an autonomous vehicle and the vehicle needs to take the next set of acions incrementally
2. A TV station headquarters receiving stream of election voting counts from various sub-stations and need to create a dashboard of the results incrementally (The KS workers for various regions like Northeast, South, etc. have specialized knowledge of how to analyze the election counts of their regions)
etc.
