from tkinter import *
import tkinter as tk

class Vehicle(object):
    def __init__(self, _speed, route, canvas):
        self.speed = _speed
        self.cLoc = route.start
        self.route = route
        self.jointCount = 0
        self.nLoc = route.joints[self.jointCount]
        self.id = None
        
        self.picEast = PhotoImage(file="resource/car-east.gif")
        self.picWest = PhotoImage(file="resource/car-west.gif")
        self.picNorth = PhotoImage(file="resource/car-north.gif")
        self.picSouth = PhotoImage(file="resource/car-south.gif")
        self.canvas = canvas
        self.__changeDirection()

    def create(self):
        #direction = self.calcDirection()
        self.id = self.canvas.create_image(self.cLoc.x+50,self.cLoc.y+50,anchor="center",image=self.photo)

    def __repr__(self):
        return "vehicle(%d)"%self.id

    def move(self):
        if self.arrived():
            print("arrived")
            self.destroy()
            return False
        if self.cLoc.x == self.nLoc.x and self.cLoc.y == self.nLoc.y:
            self.jointCount = self.jointCount + 1
            if self.jointCount == len(self.route.joints):
                self.nLoc = self.route.end
            else:
                self.nLoc = self.route.joints[self.jointCount]
            self.__changeDirection()
        self.canvas.move(self.id, self.dx, self.dy)
        self.cLoc.x = self.cLoc.x + self.dx
        self.cLoc.y = self.cLoc.y + self.dy

    def __changeDirection(self):
        direction = self.__calcDirection()
        self.dx, self.dy = 0, 0
        if direction == "north":
            self.dy = -100
            self.photo = self.picNorth
        elif direction == "south":
            self.dy = 100
            self.photo = self.picSouth
        elif direction == "east":
            self.dx = 100
            self.photo = self.picEast
        elif direction == "west":
            self.dx = -100
            self.photo = self.picWest

        if self.id is not None:
            self.canvas.itemconfigure(self.id, image=self.photo)

    def __calcDirection(self):
        if self.cLoc.x == self.nLoc.x:
            if self.cLoc.y < self.nLoc.y:
                return "south"
            else:
                return "north"
        elif self.cLoc.x < self.nLoc.x:
            return "east"
        else:
            return "west"

    def destroy(self):
        self.canvas.delete(self.id)

    def arrived(self):
        return self.cLoc.x == self.route.end.x and self.cLoc.y == self.route.end.y
