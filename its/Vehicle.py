from tkinter import *

class Vehicle(object):
    def __init__(self,_id,_speed,direction):
        self.id = _id
        self.speed = _speed
        self.direction = direction
        self.picEast = PhotoImage(file="resource/car-east.gif")
        self.picWest = PhotoImage(file="resource/car-west.gif")
        self.picNorth = PhotoImage(file="resource/car-north.gif")
        self.picSouth = PhotoImage(file="resource/car-south.gif")

    def draw(self,canvas):
        photo = self.picEast
        item = canvas.create_image(50,60,anchor=NE,image=photo)
        text = canvas.create_text(50,60, text="tk test")
                
    def __repr__(self):
        return "vehicle(%d)"%self.id
