from tkinter import *
import tkinter as tk

class Vehicle(object):
    def __init__(self,_speed, direction, canvas):
        self.speed = _speed
        self.direction = direction
        self.picEast = PhotoImage(file="resource/car-east.gif")
        self.picWest = PhotoImage(file="resource/car-west.gif")
        self.picNorth = PhotoImage(file="resource/car-north.gif")
        self.picSouth = PhotoImage(file="resource/car-south.gif")
        self.canvas = canvas
        
    def create(self):
        photo = self.picEast
        self.id = self.canvas.create_image(50,60,anchor=NE,image=photo, tag="car")
        self.canvas.create_oval(100,100,101,101,fill="black")
            
    def __repr__(self):
        return "vehicle(%d)"%self.id

    def move(self):
        dx, dy = 0, 0
        if self.direction == "north":
            dy = -1
        elif self.direction == "south":
            dy = 1
        elif self.direction == "east":
            dx = 1
        elif self.direction == "west":
            dx = -1
        self.canvas.move(self.id, dx, dy)     

    def destroy(self):
        self.canvas.delete(self.id)

    def arrived(self):
        pass
