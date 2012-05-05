from tkinter import *

class Vehicle(object):
    picEast = PhotoImage(file="car-east.gif")
    picWest = PhotoImage(file="car-est.gif")
    picNorth = PhotoImage(file="car-north.gif")
    picSouth = PhotoImage(file="car-south.gif")
    def __init__(self,_id,_speed,direction):
        self.id = _id
        self.speed = _speed
        self.direction = direction

    def draw(self,canvas):
        photo = picEast
        item = canvas.create_image(50,60,anchor=NE,image=photo)
        text = canvas.create_text(50,60, text="tk test")
                
    def __repr__(self):
        return "vehicle(%d)"%self.id
