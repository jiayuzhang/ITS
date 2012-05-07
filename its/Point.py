class Point(object):
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y

    def create(self):
        radius = 30
        loc = (self.x-radius, self.y-radius, self.x+radius, self.y+radius)
        self.canvas.draw_oval(loc, fill="black")
