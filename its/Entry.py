from Point import Point
from collections import deque

class Entry(Point):
    def __init__(self,_x,_y,_canvas):
        Point.__init__(self,_x,_y,_canvas)
        self.readyQ = deque()
        
    def hasReadyVehicle(self):
        return len(self.readyQ)>0

    #move vehicles from ready queue
    def transition(self):
        if len(self.readyQ):
            v = self.readyQ.popleft()
        if len(self.readyQ):
            self.readyQ[0].create()
        
