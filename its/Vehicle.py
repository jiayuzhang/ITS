from tkinter import *
import tkinter as tk

class Vehicle(object):
    def __init__(self, _speed, route, canvas):
        self.speed = _speed
        self.cLoc = route.start
        self.x = self.cLoc.x
        self.y = self.cLoc.y
        self.route = route
        self.jointCount = 0
        self.nLoc = route.joints[self.jointCount]
        self.id = None
        self.direction = ""
        
        self.picEast = PhotoImage(file="resource/car-east.gif")
        self.picWest = PhotoImage(file="resource/car-west.gif")
        self.picNorth = PhotoImage(file="resource/car-north.gif")
        self.picSouth = PhotoImage(file="resource/car-south.gif")
        self.canvas = canvas
        self.__changeDirection()

    def create(self):
        #direction = self.calcDirection()
        #print("%s started"%self)
        #if self.direction == "north":
        #    self.x = self.x + 9
        #elif self.direction == "south":
        #    self.x = self.x - 9
        #elif self.direction == "east":
        #    self.y = self.y + 9
        #else:
        #    self.y = self.y - 9
        self.id = self.canvas.create_image(self.x,self.y,anchor="center",image=self.photo)

    def __repr__(self):
        return "vehicle(%d)"%self.id

    def move(self):
        if self.arrived():
            self.destroy()
            return False
        if self.x == self.nLoc.x and self.y == self.nLoc.y:
            self.jointCount = self.jointCount + 1
            self.cLoc = self.nLoc
            if self.jointCount == len(self.route.joints):
                self.nLoc = self.route.end
            else:
                self.nLoc = self.route.joints[self.jointCount]
            self.__changeDirection()
        self.canvas.move(self.id, self.dx, self.dy)
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def __changeDirection(self):
        self.direction = self.__calcDirection()
        self.dx, self.dy = 0, 0
        if self.direction == "north":
            self.dy = -50
            self.photo = self.picNorth
        elif self.direction == "south":
            self.dy = 50
            self.photo = self.picSouth
        elif self.direction == "east":
            self.dx = 50
            self.photo = self.picEast
        elif self.direction == "west":
            self.dx = -50
            self.photo = self.picWest

        if self.id is not None:
            self.canvas.itemconfigure(self.id, image=self.photo)

    def __calcDirection(self):
        if self.x == self.nLoc.x:
            if self.cLoc.y < self.nLoc.y:
                return "south"
            else:
                return "north"
        elif self.x < self.nLoc.x:
            return "east"
        else:
            return "west"

    def destroy(self):
        print("%s arrived"%self)
        self.canvas.delete(self.id)

    def arrived(self):
        return self.x == self.route.end.x and self.y == self.route.end.y
