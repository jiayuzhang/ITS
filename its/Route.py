import Tkinter
class Route(object):
    def __init__(self,_start,_end,_joints,canvas):
        self.start = _start
        self.end = _end
        self.joints = _joints
        self.canvas = canvas

    def create(self):
        start = self.start
        for j in self.joints:
            end = j
            drawRoad(start,end)
            start = end
            
        drawRoad(start,self.end)

    def __repr__(self):
        pass

    def drawRoad(self, p1, p2):
        self.canvas.create_line(point1.x*100+50,point1.y*100+50,point2.x*100+50,point2.y*100+50,fill="gray", width=10, joinstyle="round", capstyle="projecting")
