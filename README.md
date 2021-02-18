# OS-Flask-API
This is the Flask API which has multiple OS-Algorithms mentioned below:
1. Cpu-Sheduling-Alorithms (Non-Preemptive only)
    1. First-Come-First-Serve (FCFS)
    2. Shortest-Job-First (SJF)
    3. Priority-Sheduling
2. Fitting-Algorithms 
    1. First-Fit
    2. Best-Fit 
    3. Worst-Fit
3. Page-Replacement-Algorithms
    1. First-In-First-Out (FIFO)
    2. Least-Recently-Used (LRU) 
    3. Optimal 
4. Bankers-Algorithm For Safety Sequence

## How To Use 
First install Flask and Flask-restful libraries
```bash 
python -m pip install flask
python -m pip install flask_restful
```
Then clone the repository
```bash
git clone https://github.com/Anushakhalil/OS-Flask-API
```
Then run the server of Flask-API
```bash 
cd OS-Flask-API
python index.py
```
### How to run Algorithms
1. Cpu-Sheduling <br/>
    Put Method:
    - Algorithms (FCFS, SJF, Priority)
    - Type (Non-p)  
    - Processes:
        - Process
        - ArrivalTime 
        - BurstTime

![1](https://github.com/Anushakhalil/OS-Flask-API/blob/main/images/Cpu-Sheduling.png "Example image for Cpu-Sheduling")

2. Fitting <br/>
    put Method:
    - Type
    - ReadyQueue
    - Processes:
        - Process
        - Size

![2](https://github.com/Anushakhalil/OS-Flask-API/blob/main/images/Fitting.png "Example image for Fitting")

3. Page-Replacement <br/>
    Put Method:
    - Type
    - frames
    - ReferenceString

![3](https://github.com/Anushakhalil/OS-Flask-API/blob/main/images/PageReplacement.png "Example image for PageReplacement")

4. Bankers-Algorithm <br/>
    Put Method:
    - TotalWorkVector
    - AvailableWorkVector
    - Processes:
        - Process
        - need
        - allocated

![4](https://github.com/Anushakhalil/OS-Flask-API/blob/main/images/bankers.png "Example image for bankers")

### Important Guidelines
- While using Postman make sure to add the processes through raw data with JSON field selected.
- The written fields in every put method are case sensitve.

![5](https://github.com/Anushakhalil/OS-Flask-API/blob/main/images/DataEnterExample.png "Data Enter Example")