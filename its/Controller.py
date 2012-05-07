from Entry import Entry
from Joint import Joint
from Generator import Generator
from Route import Route
from math import *

class Controller(object):
    def __init__(self, _config, _canvas):
        self.canvas = _canvas
        self.entrys = []
        self.joints = []
        self.graph = None

        self.parseConfiguration(_config)
        self.initCanvas()

        self.gen = Generator([i for i in range(len(self.entrys))],self.graph)
        self.readyQ = []
        self.runningQ = []

    def parseConfiguration(self,fileName):
        X,Y = 0,1
        inFile = open(fileName, "r")
        for line in inFile:
            line = line.strip("\n")
            if line == "#count":
                entryCnt = int(inFile.readline().strip("\n")[6:]) #entry=.. no pairs of entry connected
                jointCnt = int(inFile.readline().strip("\n")[6:]) #joint=.. at least one joint
                self.graph = [[0]*(entryCnt+jointCnt) for i in range(entryCnt+jointCnt)] #adj matrix
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
                        self.graph[i][entryCnt+j] = self.graph[entryCnt+j][i] = True if int(tokens[j])==1 else False
            elif line == "#joint_joint":
                for i in range(jointCnt):
                    tokens = inFile.readline().strip("\n").split()
                    for j in range(jointCnt):
                        if i != j:
                            self.graph[entryCnt+i][entryCnt+j] = self.graph[entryCnt+j][entryCnt+i] = self.calcDistance(self.joints[i],self.joints[j]) if int(tokens[j])==1 else -1

    def calcDistance(self,p1,p2):
        return int(sqrt(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2)))


    def initCanvas(self):
        print("##########################")
        #for entry in self.entrys:
        #    entry.draw(self.canvas)
        #for joint in self.joints:
        #   joint.draw(self.canvas)

        entrySize = len(self.entrys)
        jointSize = len(self.joints)
        size = entrySize + jointSize
        print(size)
        for i in range(size):
            print(i)
            for j in range(i+1,size):
                if self.graph[i][j] > 0:
                    point1 = self.entrys[j] if j < entrySize else self.joints[j-entrySize]
                    point2 = self.entrys[i] if i < entrySize else self.joints[i-entrySize]

                    #self.canvas.create_line(point1.x*100+50,point1.y*100+50,point2.x*100+50,point2.y*100+50,fill="black", width=12, joinstyle="round", capstyle="projecting")
                    self.canvas.create_line(point1.x*100+50,point1.y*100+50,point2.x*100+50,point2.y*100+50,fill="gray", width=10, joinstyle="round", capstyle="projecting")

    
    def tick(self):
        #do logic on models
        #call each existing model draw method by passing canvas
        startIdx,endIdx,jointIdxAry = self.gen.genVehicle()
        r = Route(self.entrys[startIdx],self.entrys[endIdx],[self.joints[i-len(self.entrys)] for i in jointIdxAry])
        self.readyQ.append(Vehicle(5,r,self.canvas))


        
        
