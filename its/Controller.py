from Entry import Entry
from Joint import Joint

class Controller(object):
    def __init__(self, _config, _canvas):
        self.canvas = _canvas
        self.entrys = []
        self.joints = []
        self.graph = None

        self.parseConfiguration(_config)
        self.initCanvas()

    def parseConfiguration(self,fileName):
        X,Y = 0,1
        inFile = open(fileName, "r")
        for line in inFile:
            line = line.strip("\n")
            if line == "#count":
                entryCnt = int(inFile.readline().strip("\n")[6:]) #entry=.. no pairs of entry connected
                jointCnt = int(inFile.readline().strip("\n")[6:]) #joint=.. at least one joint
                self.graph = [[False]*(entryCnt+jointCnt) for i in range(entryCnt+jointCnt)] #adj matrix
            elif line == "#entry":
                for i in range(entryCnt):
                    coords = [int(token) for token in inFile.readline().strip("\n").split()]
                    self.entrys.append(Entry(coords[X],coords[Y]))
            elif line == "#joint":
                for i in range(jointCnt):
                    coords = [int(token) for token in inFile.readline().strip("\n").split()]
                    self.joints.append(Joint(coords[X],coords[Y]))
            elif line == "#entry_joint":
                for i in range(entryCnt):
                    tokens = inFile.readline().strip("\n").split()
                    for j in range(jointCnt):
                        self.graph[i][entryCnt+j] = self.graph[entryCnt+j][i] = True if int(tokens[j])==1 else False
            elif line == "#joint_joint":
                for i in range(jointCnt):
                    tokens = inFile.readline().strip("\n").split()
                    for j in range(jointCnt):
                        self.graph[entryCnt+i][entryCnt+j] = self.graph[entryCnt+j][entryCnt+i] = True if int(tokens[j])==1 else False

    def initCanvas(self):
        #print("##########################")
        #for entry in self.entrys:
        #    entry.draw(self.canvas)
        #for joint in self.joints:
        #   joint.draw(self.canvas)

        entrySize = len(self.entrys)
        jointSize = len(self.joints)
        size = entrySize + jointSize
        for i in range(size):
            for j in range(i+1,size):
                if self.graph[i][j]:
                    point1,point2 = self.entrys[i] if i < entrySize else self.joints[i-entrySize],self.entrys[j] if j < entrySize else self.joints[j-entrySize]
                    self.canvas.create_line(point1.x,point2.y,point2.x,point2.y,fill="black")
        
    
    def tick(self):
        #do logic on models
        #call each existing model draw method by passing canvas
        pass
