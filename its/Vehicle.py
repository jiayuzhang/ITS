from tkinter import *

class Vehicle(object):
    def __init__(self,_speed,direction):
        self.speed = _speed
        self.direction = direction
        self.picEast = PhotoImage(file="resource/car-east.gif")
        self.picWest = PhotoImage(file="resource/car-west.gif")
        self.picNorth = PhotoImage(file="resource/car-north.gif")
        self.picSouth = PhotoImage(file="resource/car-south.gif")
        

    def draw(self,canvas):
        photo = self.picEast
        self.id = canvas.create_image(50,60,anchor=NE,image=photo, tag="car")
        text = canvas.create_text(50,60, text="tk test")
        canvas.create_oval(100,100,101,101,fill="black")
                
    def __repr__(self):
        return "vehicle(%d)"%self.id

    def move(self):
        dy, dx = 0, 0
        if direction == "north":
            dy = -1
        elif direction == "south":
            dy = 1
        elif direction == "east":
            dx = 1
        elif direction == "west":
            dx = -1
        move(self.id, dx, dy)
