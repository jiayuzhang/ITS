import random as r

class Generator(object):
    def __init__(self, _entryIds, _adjcencyMatrix):
        self.eids = _entryIds
        self.m = _adjcencyMatrix
        self.shortPath = {}
        self.floydWarshallForAllEntrys()

    def cost(self,i,j):
        if self.m[i][j] == -1:
            return 10000 #assume it is max int
        else:
            return self.m[i][j]

    def floydWarshallForAllEntrys(self):
        n = len(self.m)
        path = [[0]*n for i in range(n)]
        node = [[-1]*n for i in range(n)]
        for row in range(n):
            for col in range(n):
                path[row][col] = self.cost(row,col)
                node[row][col] = col if self.cost(row,col)>=0 else -1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if path[i][k]+path[k][j] < path[i][j]:
                        path[i][j] = path[i][k]+path[k][j]
                        node[i][j] = k

        for i in range(len(self.eids)):
            for j in range(i+1,len(self.eids)):
                self.shortPath[(self.eids[i],self.eids[j])] = self.getPath(self.eids[i],self.eids[j],node)
                self.shortPath[(self.eids[j],self.eids[i])] = self.getPath(self.eids[j],self.eids[i],node)
    

    def getPath(self,i,j,node):
        if node[i][j] == -1:
            return None
        k = node[i][j]
        if k == j:
            return []
        else:
            return self.getPath(i,k,node) + [k] + self.getPath(k,j,node)

    def genVehicle(self):
        start,end = r.choice(self.eids),r.choice(self.eids)
        while start == end:
            end = r.choice(self.eids)
        return start,end,self.shortPath[(start,end)]

