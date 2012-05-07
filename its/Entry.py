from Point import Point
from collections import deque

class Entry(Point):
    def __init__(self,_x,_y,_canvas):
        Point.__init__(self,_x,_y,_canvas)
        self.readyQ = deque()
        self.id = self.canvas.create_text(self.x, self.y-25, text=len(self.readyQ))
        
    def hasReadyVehicle(self):
        return len(self.readyQ)>0

    def peekVehicle(self):
        return self.readyQ[0]
    
    #move vehicles from ready queue
    def popVehicle(self):
        if len(self.readyQ):
            v = self.readyQ.popleft()
        if len(self.readyQ):
            self.readyQ[0].create()
        self.update()
        return v

    def appendVehicle(self,v):
        self.readyQ.append(v)
        if len(self.readyQ) == 1:
            v.create()
        #draw the upper corner number
        self.update()
    
    def update(self):
        self.canvas.itemconfigure(self.id, text=len(self.readyQ))
