from Entry import Entry
from Joint import Joint
from Generator import Generator
from Route import Route
from Vehicle import Vehicle
from math import *
import random

class Controller(object):
    def __init__(self, _config, _canvas):
        self.canvas = _canvas
        self.entrys = []
        self.joints = []
        self.graph = None

        self.parseConfiguration(_config)
        self.initCanvas()
        
        self.gen = Generator([i for i in range(len(self.entrys))],self.graph)
        self.runningQ = []

        self.inc = 0

    def parseConfiguration(self,fileName):
        X,Y = 0,1
        inFile = open(fileName, "r")
        for line in inFile:
            line = line.strip("\n")
            if line == "#count":
                entryCnt = int(inFile.readline().strip("\n")[6:]) #entry=.. no pairs of entry connected
                jointCnt = int(inFile.readline().strip("\n")[6:]) #joint=.. at least one joint
                self.graph = [[-1]*(entryCnt+jointCnt) for i in range(entryCnt+jointCnt)] #adj matrix
            elif line == "#entry":
                for i in range(entryCnt):
                    coords = [int(token) for token in inFile.readline().strip("\n").split()]
                    self.entrys.append(Entry(coords[X],coords[Y],self.canvas))
            elif line == "#joint":
                for i in range(jointCnt):
                    coords = [int(token) for token in inFile.readline().strip("\n").split()]
                    self.joints.append(Joint(coords[X],coords[Y],self.canvas))
            elif line == "#entry_joint":
                for i in range(entryCnt):
                    tokens = inFile.readline().strip("\n").split()
                    for j in range(jointCnt):
                        self.graph[i][entryCnt+j] = self.graph[entryCnt+j][i] = self.calcDistance(self.entrys[i],self.joints[j]) if int(tokens[j])==1 else -1
            elif line == "#joint_joint":
                for i in range(jointCnt):
                    tokens = inFile.readline().strip("\n").split()
                    for j in range(jointCnt):
                        if i != j:
                            self.graph[entryCnt+i][entryCnt+j] = self.graph[entryCnt+j][entryCnt+i] = self.calcDistance(self.joints[i],self.joints[j]) if int(tokens[j])==1 else -1

    def calcDistance(self,p1,p2):
        return int(sqrt(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2)))


    def initCanvas(self):
        #for entry in self.entrys:
        #    entry.draw(self.canvas)
        #for joint in self.joints:
        #   joint.draw(self.canvas)

        entrySize = len(self.entrys)
        jointSize = len(self.joints)
        size = entrySize + jointSize
        for i in range(size):
            for j in range(i+1,size):
                if self.graph[i][j] > 0:
                    point1 = self.entrys[j] if j < entrySize else self.joints[j-entrySize]
                    point2 = self.entrys[i] if i < entrySize else self.joints[i-entrySize]

                    #self.canvas.create_line(point1.x*100+50,point1.y*100+50,point2.x*100+50,point2.y*100+50,fill="black", width=12, joinstyle="round", capstyle="projecting")
                    self.canvas.create_line(point1.x,point1.y,point2.x,point2.y,fill="gray", width=40, joinstyle="round", capstyle="projecting")

    def automate(self):
        if random.random() < 0.5:
        #   print("start automate")
            startIdx,endIdx,jointIdxAry = self.gen.genVehicle()
            r = Route(self.entrys[startIdx],self.entrys[endIdx],[self.joints[i-len(self.entrys)] for i in jointIdxAry])
            v = Vehicle(self.inc,r,self.canvas)
            self.entrys[startIdx].appendVehicle(v)
        #   print("Entry%d add %s"%(startIdx,v))
        #   print("after automate")
            
    def tick(self):
        print("---------------------------------------------------")
        #do logic on models
        #call each existing model draw method by passing canvas
        self.automate()

        #for i,e in enumerate(self.entrys):
        #    print("%d Entry %s"%(i,str(e.readyQ)))
        
        #go through all entrys with at least one ready vehicle
        vehicleCandidates = [e.peekVehicle() for e in self.entrys if e.hasReadyVehicle()]

        #main logic, calculate based on current running v and candidate v
        self.runningQ += vehicleCandidates

        
        for v in vehicleCandidates:
        #    print("%s starts"%v)
            v.route.start.popVehicle()
        
        print(self.runningQ)
        #
        for v in self.runningQ:
            v.move()
        #self.runningQ[:] = [v for v in self.runningQ if v.move()]

        
        
        
