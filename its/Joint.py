from Point import Point

class Joint(Point):
    def __init__(self,_x,_y,_canvas):
        Point.__init__(self,_x,_y,_canvas)
        self.timeRecord = set()
        self.tmpTimeRecord = {}
        self.tmpReverseTimeRecord = {}

    def dec(self):
        if len(self.timeRecord):
            self.timeRecord = set([tm-50 for tm in self.timeRecord if tm>50])
