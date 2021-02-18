class Algorithms:
    def FCFS(self,jobQueue):
        output =str()
        # jobQueue = [
        # {
        #     "Process":"P1",
        #     "BurstTime": 50+(50*1),
        #     "ArrivalTime":0
        # },
        # {
        #     "Process":"P2",
        #     "BurstTime": 51+(50*2),
        #     "ArrivalTime":0
        # },
        # {
        #     "Process":"P3",
        #     "BurstTime": 52+(50*3),
        #     "ArrivalTime":0
        # },
        # {
        #     "Process":"P4",
        #     "BurstTime": 53+(50*4),
        #     "ArrivalTime":0
        # },

        # ]

        for i in jobQueue:
            output+=str(i)+"\n"

        readyQueue = []
        waitingQueue = []

        CPU_process_record = []

        time = 0

        while jobQueue != [] or readyQueue != [] or waitingQueue != []:
            lstOfDeletion = []
            for j, i in enumerate(jobQueue):

                if i["ArrivalTime"] <= time:

                    readyQueue.append(i)
                    lstOfDeletion.append(i)

            for i in lstOfDeletion:
                jobQueue.remove(i)

            lstOfDeletion = []

            for j in readyQueue:
                lstOfDeletion.append(j)
                startTime = time
                time += j["BurstTime"]
                CPU_process_record.append({"Process":j["Process"], "StartTime":startTime, "EndTime":time})
            for j in lstOfDeletion:
                readyQueue.remove(j)

        output+="First Come First Serve \n"
        SumOfStartTime = 0
        SumOfEndTime = 0
        for i in CPU_process_record:
            output+=str(i)+"\n"
            SumOfStartTime += i["StartTime"]
            SumOfEndTime += i["EndTime"]

        AvgTime = SumOfStartTime/len(CPU_process_record)
        turnAround = SumOfEndTime/len(CPU_process_record)
        output+="Average Waiting Time: "+str(AvgTime)+" Units \n"
        output+="Average TurnAround Time: "+str(turnAround)+ " Units \n "
        return output

    def SJF_Non_Premptive(self,jobQueue):
        output= str()
    #     jobQueue = [
    #     {
    #         "Process":"P1",
    #         "BurstTime": 4,
    #         "ArrivalTime":0
    #     },
    #     {
    #         "Process":"P2",
    #         "BurstTime": 8,
    #         "ArrivalTime":0
    #     },
    #     {
    #         "Process":"P3",
    #         "BurstTime": 3,
    #         "ArrivalTime":0
    #     },
    #     {
    #         "Process":"P3",
    #         "BurstTime": 7,
    #         "ArrivalTime":0
    #     },

    # ]

    # print("Job Queue initially")
        output+="Job Queue initially \n"
        for i in jobQueue:
            # print(i)
            output+=str(i)+"\n"
        readyQueue = []
        waitingQueue = []

        CPU_process_record = []

        time = min([process["ArrivalTime"] for process in jobQueue ])

        while jobQueue != [] or readyQueue != [] or waitingQueue != []:
            lstOfDeletion = []
            for j, i in enumerate(jobQueue):

                if i["ArrivalTime"] <= time:

                    readyQueue.append(i)
                    lstOfDeletion.append(i)

            for i in lstOfDeletion:
                jobQueue.remove(i)

            lstOfDeletion = []

            listOfBurstTimes = [process["BurstTime"] for process in readyQueue]
            sortedListOfBurstTimes = sorted(listOfBurstTimes)

            sortedReadyQueue = [process for burst in sortedListOfBurstTimes for process in readyQueue if process["BurstTime"] == burst]

            # sortedReadyQueue = []



            for process in sortedReadyQueue:
                readyQueue.remove(process)


            for j in sortedReadyQueue:
                lstOfDeletion.append(j)
                startTime = time
                time += j["BurstTime"]
                CPU_process_record.append({"Process":j["Process"], "StartTime":startTime, "EndTime":time})
            for j in lstOfDeletion:
                sortedReadyQueue.remove(j)

        output+="Shortest Job First \n"
        SumOfStartTime = 0
        SumOfEndTime = 0
        for i in CPU_process_record:
            # print(i)
            output+=str(i)+"\n"

            SumOfStartTime += i["StartTime"]
            SumOfEndTime += i["EndTime"]

        AvgTime = SumOfStartTime/len(CPU_process_record)
        turnAround = SumOfEndTime/len(CPU_process_record)
        # print("Average Waiting Time: ",AvgTime," Units")
        # print("Average TurnAround Time: ", turnAround, " Units")
        output+="Average Waiting Time: "+str(AvgTime)+" Units \n"
        output+="Average TurnAround Time: "+str(turnAround)+ " Units \n"
        return output

    def Priority(self,jobQueue):
#         jobQueue = [
#     {
#         "Process":"P1",
#         "BurstTime": 4,
#         "ArrivalTime":0,
#         "Priority": 2
#     },
#     {
#         "Process":"P2",
#         "BurstTime": 8,
#         "ArrivalTime":0,
#         "Priority": 1
#     },
#     {
#         "Process":"P3",
#         "BurstTime": 3,
#         "ArrivalTime":0,
#         "Priority":4
#     },
#     {
#         "Process":"P4",
#         "BurstTime": 7,
#         "ArrivalTime":0,
#         "Priority":3
#     },

# ]
        output=str()
        output+="Job Queue initially \n"
        for i in jobQueue:
            output+=str(i)+"\n"

        readyQueue = []
        waitingQueue = []

        CPU_process_record = []

        time = min([process["ArrivalTime"] for process in jobQueue ])

        while jobQueue != [] or readyQueue != [] or waitingQueue != []:
            lstOfDeletion = []
            for j, i in enumerate(jobQueue):

                if i["ArrivalTime"] <= time:

                    readyQueue.append(i)
                    lstOfDeletion.append(i)

            for i in lstOfDeletion:
                jobQueue.remove(i)

            lstOfDeletion = []

            listOfPriority = [process["Priority"] for process in readyQueue]
            sortedListOfPriority = sorted(listOfPriority)

            sortedReadyQueue = [process for priority in sortedListOfPriority for process in readyQueue if process["Priority"] == priority]

            # sortedReadyQueue = []



            for process in sortedReadyQueue:
                readyQueue.remove(process)


            for j in sortedReadyQueue:
                lstOfDeletion.append(j)
                startTime = time
                time += j["BurstTime"]
                CPU_process_record.append({"Process":j["Process"], "StartTime":startTime, "EndTime":time})
            for j in lstOfDeletion:
                sortedReadyQueue.remove(j)

        output+="Priority \n"
        SumOfStartTime = 0
        SumOfEndTime = 0
        for i in CPU_process_record:
            output+=str(i)+"\n"
            SumOfStartTime += i["StartTime"]
            SumOfEndTime += i["EndTime"]

        AvgTime = SumOfStartTime/len(CPU_process_record)
        turnAround = SumOfEndTime/len(CPU_process_record)
        output+="Average Waiting Time: "+str(AvgTime)+" Units \n"
        output+="Average TurnAround Time: "+str(turnAround)+ " Units \n"
        return output

def Bankers(resourcesTotal,resourcesAvailable,processes):
    from operator import add
    output=str()
    # processes = [
    #     {
    #         "Process":"P0",
    #         "need":[7,4,3],
    #         "allocated":[0,1,0]
    #     },
    #     {
    #         "Process":"P1",
    #         "need":[1,2,2],
    #         "allocated":[2,0,0]
    #     },
    #     {
    #         "Process":"P2",
    #         "need":[6,0,0],
    #         "allocated":[3,0,2]
    #     },
    #     {
    #         "Process":"P3",
    #         "need":[0,1,1],
    #         "allocated":[2,1,1]
    #     },
    #     {
    #         "Process":"P4",
    #         "need":[4,3,1],
    #         "allocated":[0,0,2]
    #     }
    # ]

    work= resourcesAvailable
    # resourcesTotal= [10,5,7]

    for process in processes:
        process["finish"] = False

    n = 0
    safetySequence = []

    while all([process["finish"] for process in processes]) != True:
        if n>0:
            lstOfProcesses = [process for process in processes if process["finish"] == False][::-1]
        else:
            lstOfProcesses = [process for process in processes if process["finish"] == False]

        # print(f"{n} -----> {lstOfProcesses}")

        for process in lstOfProcesses:
            # print(f"PROCESS --> {process}")
            if process["need"] <= work:
                process["finish"] = True
                work = list(map(add,work,process["need"]))
                safetySequence.append(process["Process"])
        n+=1

        if n>10:
            safe = False
            break
        else:
            safe = True


    output+=str(["SAFE" if safe else "UNSAFE" for safe in [safe]][0])
    output+=f"\n SAFETY SEQUENCE {safetySequence}"
    return output

class Fitting:
    def first_fit(self,processes,readyQueue):
        output=str()
        ReadyQueueRecord=[]
        UnScheduledProcesses = []

        # FIRST FIT
        for process in processes:
            if readyQueue != [] and max(readyQueue) >= process["Size"]:

                for memory in readyQueue:
                    if memory > process["Size"]:
                        ReadyQueueRecord.append({
                            "Process":process["Process"],
                            "Location":memory,
                            "Usage":process["Size"],
                            "Wastage":memory - process["Size"]
                        })
                        m = memory
                        break
                readyQueue.remove(m)
            else:
                UnScheduledProcesses.append(
                    process
                )
        # print("\n\n------ FIRST FIT ------")
        for i in ReadyQueueRecord:
            output+=str(i)+"\n"

        output+="UNSCHEDULED \n"
        for j in UnScheduledProcesses:
            output+=str(i)+"\n"
        output+="\nTOTAL WASTAGE OF FIRST FIT: "+ str(sum([process["Wastage"] for process in ReadyQueueRecord ]))
        return output

        
    def best_fit(self,processes,readyQueue):
        ReadyQueueRecord=[]
        UnScheduledProcesses = []
        output=str()
        #BEST FIT
        for process in processes:
            if readyQueue !=[] and max(readyQueue) >= process["Size"]:
                dummyList = readyQueue
                while(True):
                    if min(dummyList) >= process["Size"]:
                        ReadyQueueRecord.append({
                            "Process":process["Process"],
                            "Location":min(dummyList),
                            "Usage":process["Size"],
                            "Wastage":min(dummyList) - process["Size"]
                        })
                        readyQueue.remove(min(dummyList))
                        break
                    else:
                        dummyList.remove(min(dummyList))
            else:
                UnScheduledProcesses.append(
                    process
                )
        # print("\n\n------ BEST FIT ------")
        for i in ReadyQueueRecord:
            output+=str(i)+"\n"

        output+="UNSCHEDULED \n"
        for j in UnScheduledProcesses:
            output+=str(j)+"\n"
        output+="\nTOTAL WASTAGE OF BEST FIT: "+ str(sum([process["Wastage"] for process in ReadyQueueRecord ]))
        return output

    def worst_fit(self,processes,readyQueue):
        ReadyQueueRecord=[]
        UnScheduledProcesses = []
        output=str()
    #WORST FIT
        for process in processes:
            if readyQueue != [] and max(readyQueue) >= process["Size"]:
                ReadyQueueRecord.append({
                    "Process": process["Process"],
                    "Location": max(readyQueue),
                    "Usage": process["Size"],
                    "Wastage":max(readyQueue) - process["Size"]
                })
                readyQueue.remove(max(readyQueue))
            else:
                UnScheduledProcesses.append(process)
        # print("\n\n------ WORST FIT ------")
        for i in ReadyQueueRecord:
            output+=str(i)+"\n"

        output+="UNSCHEDULED \n"
        for j in UnScheduledProcesses:
            output+=str(j)+"\n"
        output+="\nTOTAL WASTAGE OF WORST FIT: "+ str(sum([process["Wastage"] for process in ReadyQueueRecord ]))
        return output


class Paging:
    def Fifo(self,string,frames):
        output=str()
        faults = 0
        lst = []
        L = len(string)
        notFaults = 0
        index = 0
        output+="---------- FIFO PAGE REPLACEMENT ALGORITHM ----------\n "
        output+="REFERENCE STRING:"+ string +"\n"
        while L:
            for i,v in enumerate(string):
                if (i+1)<= frames and v not in lst:
                    lst.append(v)
                    faults +=1
                    L-=1
                else:
                    if v not in lst:
                        lst[index]=v
                        faults+=1
                        L-=1
                        if index < (frames - 1):
                            index += 1
                        else:
                            index = 0

                    else:
                        L-=1
                        notFaults+=1
                output+=str(lst)+"\n"

        f= faults + notFaults
        output+="Total frames: "+str(f)+"\n"
        output+="Page faults: "+str(faults)
        return output
        
    def LRU(self,reference_string,No_of_frames):
    # reference_string = "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1"

# No_of_frames = 3
        output= str()
        lstOfFrames = [None] * No_of_frames

        referenceLst = [value for value in reference_string]
        output+="---------- LRU PAGE REPLACEMENT ALGORITHM ----------\n"
        output+=f"REFERENCE STRING: {reference_string} \n"

        pageFaults = 0
        for index,i in enumerate(referenceLst):
            if None in lstOfFrames:
                lstOfFrames[lstOfFrames.index(None)] = i
                pageFaults += 1
            else:
                if i in lstOfFrames:
                    pass
                else:
                    toReplace = referenceLst[:index][::-1][max([referenceLst[:index][::-1].index(number)  if number in referenceLst[:index][::-1] else len(referenceLst) for number in lstOfFrames ])]
                    lstOfFrames[lstOfFrames.index(toReplace)] = i
                    pageFaults += 1

            output+="List of frames:" + str(lstOfFrames) +"Page Faults" +str(pageFaults)+"\n"


        output+=f"PAGE FAULT: {pageFaults}"
        return output

    def Optimal(self,reference_string,No_of_frames):
        # reference_string = "2 3 4 2 1 3 7 5 4 3"

        # No_of_frames = 4
        output=str()
        lstOfFrames = [None] * No_of_frames

        referenceLst = [value for value in reference_string]
        output+="---------- OPTIMAL PAGE REPLACEMENT ALGORITHM ----------\n"
        output+=f"REFERENCE STRING: {reference_string} \n"

        pageFaults = 0
        for index,i in enumerate(referenceLst):
            if None in lstOfFrames:
                lstOfFrames[lstOfFrames.index(None)] = i
                pageFaults += 1
            else:
                if i in lstOfFrames:
                    pass
                else:
                    NoOfElementsFound = len([True for i in lstOfFrames if i not in referenceLst[index+1:]])
                    if NoOfElementsFound == 1:
                        elementNotFound = str([element for element in lstOfFrames if element not in referenceLst[index+1:]][0])
                        toReplace = elementNotFound
                    elif NoOfElementsFound > 1:
                        elementsNotFound = [element for element in lstOfFrames if element not in referenceLst[index + 1:]]
                        toReplace = referenceLst[:index][::-1][max([referenceLst[:index][::-1].index(number) for number in elementsNotFound])]
                    else:
                        toReplace = referenceLst[index+1:][max([referenceLst[index+1:].index(number) for number in lstOfFrames])]

                    lstOfFrames[lstOfFrames.index(toReplace)] = i
                    pageFaults += 1

            output+="List of frames" + str(lstOfFrames) +"Page Faults"+ str(pageFaults)+"\n"


        output+=f"PAGE FAULT: {pageFaults}"
        return output



    



