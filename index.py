from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from Algorithms import Algorithms, Bankers, Fitting, Paging
import ast

alg_obj=Algorithms()
app = Flask(__name__)
api = Api(app)

alg_put = reqparse.RequestParser()
alg_put.add_argument("Algorithm",type=str)
alg_put.add_argument("Type",type=str)
alg_put.add_argument("Processes",type=str)
alg_put.add_argument("QuantNo",type=int)
alg_put.add_argument("Output",type=str)

CpuSheduling = {1 :  {"Algorithm" : "FCFS", "Type" : "Non-p","Processes" : {1:{"Process":"P1","ArrivalTime": 0,"BurstTime": 5}}}}
def notFound(alg_id):
    if alg_id not in CpuSheduling:
        abort(404, message="Record not found!")

class Alg(Resource):
    def get(self, alg_id):
        notFound(alg_id)
        return CpuSheduling[alg_id]["Output"]

    def put(self,alg_id):
        newAlg = alg_put.parse_args()
        CpuSheduling[alg_id] = newAlg
        record= CpuSheduling[alg_id]
        if record["Type"] == "Non-p":
            if record["Algorithm"] == "SJF":
                process=ast.literal_eval(record["Processes"])
                jobQueue= [value for value in process.values()]
                record["Output"]=alg_obj.SJF_Non_Premptive(jobQueue)
                return record
            elif record["Algorithm"] == "FCFS":
                process=ast.literal_eval(record["Processes"])
                jobQueue= [value for value in process.values()]
                record["Output"]=alg_obj.FCFS(jobQueue)
                return record
            elif record["Algorithm"] == "Priority":
                process=ast.literal_eval(record["Processes"])
                jobQueue= [value for value in process.values()]
                record["Output"]=alg_obj.Priority(jobQueue)
                return record
        else:
            return "Work under construction."

    def delete(self, alg_id):
        del CpuSheduling[alg_id]
        return '', 204
#--------------------------------------------- bankers section ----------------------------------------

bnk_put = reqparse.RequestParser()
bnk_put.add_argument("TotalWorkVector",type=str)
bnk_put.add_argument("AvailableWorkVector",type=str)
bnk_put.add_argument("Processes",type=str)
bnk_put.add_argument("Output",type=str)

bankers = {1 :  {"TotalWorkVector" : [3,3,2], "AvailableWorkVector" : [10,5,7],"Processes" : {1:{"Process":"P1","need": [7,4,3],"allocated": [0,1,0]}}}}

def notFound(alg_id):
    if alg_id not in bankers:
        abort(404, message="Record not found!")

class bankersAlg(Resource):
    def get(self, alg_id):
        notFound(alg_id)
        return bankers[alg_id]["Output"]

    def put(self,alg_id):
        newAlg = bnk_put.parse_args()
        bankers[alg_id] = newAlg
        record= bankers[alg_id]
        process=ast.literal_eval(record["Processes"])
        processes= [value for value in process.values()]
        record["Output"]= Bankers(ast.literal_eval(record["TotalWorkVector"]),ast.literal_eval(record["AvailableWorkVector"]),processes)
        return record

    def delete(self, alg_id):
        del bankers[alg_id]
        return '', 204
# ------------------------- memory management --------------------------------------

mem_put = reqparse.RequestParser()
mem_put.add_argument("Type",type=str)
mem_put.add_argument("ReadyQueue",type=str)
mem_put.add_argument("Processes",type=str)
mem_put.add_argument("Output",type=str)

fitting = {1 :  {"Type":"FIRST","ReadyQueue" : [100,500,200,300,600],"Processes" : {1:{"Process":"P1","size":212}}}}
fit_obj=Fitting()

def notFound(alg_id):
    if alg_id not in fitting:
        abort(404, message="Record not found!")

class FittingAlg(Resource):
    def get(self, alg_id):
        notFound(alg_id)
        return fitting[alg_id]["Output"]

    def put(self,alg_id):
        newAlg = mem_put.parse_args()
        fitting[alg_id] = newAlg
        record= fitting[alg_id]
        process=ast.literal_eval(record["Processes"])
        processes= [value for value in process.values()]
        readyq= ast.literal_eval(record["ReadyQueue"])
        if record["Type"] == "FIRST":
            record["Output"]= fit_obj.first_fit(processes,readyq)
        elif record["Type"] == "BEST":
            record["Output"]= fit_obj.best_fit(processes,readyq)
        elif record["Type"] == "WORST":
            record["Output"]= fit_obj.worst_fit(processes,readyq)
        return record

    def delete(self, alg_id):
        del fitting[alg_id]
        return '', 204

#    ----------------------------- paging ---------------------------------

pg_put = reqparse.RequestParser()
pg_put.add_argument("Type",type=str)
pg_put.add_argument("frames",type=int)
pg_put.add_argument("ReferenceString",type=str)
pg_put.add_argument("Output",type=str)

paging = {1 :  {"Type":"FIFO","frames":3,"ReferenceString":"70120304230321201701"}}
pg_obj=Paging()

def notFound(alg_id):
    if alg_id not in paging:
        abort(404, message="Record not found!")

class PagingAlg(Resource):
    def get(self, alg_id):
        notFound(alg_id)
        return paging[alg_id]["Output"]

    def put(self,alg_id):
        newAlg = pg_put.parse_args()
        paging[alg_id] = newAlg
        record= paging[alg_id]
        frame= record["frames"]
        string= record["ReferenceString"]
        if record["Type"] == "FIFO":
            record["Output"]= pg_obj.Fifo(string,frame)
        elif record["Type"] == "LRU":
            record["Output"]= pg_obj.LRU(string,frame)
        elif record["Type"] == "OPTIMAL":
            record["Output"]= pg_obj.Optimal(string,frame)
        return record

    def delete(self, alg_id):
        del paging[alg_id]
        return '', 204

api.add_resource(Alg, "/cpu-sheduling/<int:alg_id>")   # represent route
api.add_resource(bankersAlg,"/bankers-algorithm/<int:alg_id>") # represent
api.add_resource(FittingAlg,"/fitting-algorithm/<int:alg_id>")
api.add_resource(PagingAlg,"/paging-algorithm/<int:alg_id>")
if __name__ == '__main__':
    app.run(debug=True)
