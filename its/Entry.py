from Point import Point
from collections import deque

class Entry(Point):
    def __init__(self,_x,_y,_canvas):
        Point.__init__(self,_x,_y,_canvas)
        self.readyQ = deque()
        
    def hasReadyVehicle(self):
        return len(self.readyQ)>0

    def peekVehicle(self):
        return self.readyQ[0]
    
    #move vehicles from ready queue
    def popVehicle(self):
        if len(self.readyQ):
            self.readyQ.popleft()
        if len(self.readyQ):
            self.readyQ[0].create()

    def appendVehicle(self,v):
        self.readyQ.append(v)
        if len(self.readyQ) == 1:
            v.create()
        #draw the upper corner number
    
