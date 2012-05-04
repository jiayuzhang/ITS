from Tkinter import *
class Vehicle(object):
    def __init__(self,_id,_speed):
        self.id = _id
        self.speed = _speed

    def draw(self,canvas):
	photo =  PhotoImage(file="car.gif")
	item = canvas.create_image(50,50,image=photo)

    def __repr__(self):
        return "vehicle(%d)"%self.id
