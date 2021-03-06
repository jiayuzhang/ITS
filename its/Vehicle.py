from tkinter import *
import tkinter as tk
import random

class Vehicle(object):
    def __init__(self, _speed, route, canvas, _widthRadio, _heightRadio):
        self.wr = _widthRadio
        self.hr = _heightRadio
        self.speed = _speed
        self.cLoc = route.start
        self.x = self.cLoc.x
        self.y = self.cLoc.y
        self.route = route
        self.jointCount = 0
        self.nLoc = route.joints[self.jointCount]
        self.id = None
        self.offsetX = 0
        self.offsetY = 0
        self.direction = ""
        imgname = "resource/car"+str(random.randrange(1,5))
        self.picEast = PhotoImage(file=imgname+"-east.gif")
        self.picWest = PhotoImage(file=imgname+"-west.gif")
        self.picNorth = PhotoImage(file=imgname+"-north.gif")
        self.picSouth = PhotoImage(file=imgname+"-south.gif")
        self.canvas = canvas
        self.__changeDirection()
        self.dx *= self.wr
        self.dy *= self.hr
        
    def create(self):
        #direction = self.calcDirection()
        #print("%s started"%self)
        #print("create")
        self.id = self.canvas.create_image(self.x + self.offsetX,self.y + self.offsetY,image=self.photo)
        #self.canvas.update()
        #self.text = self.canvas.create_text(self.x + self.offsetX,self.y + self.offsetY-30, text=self.id)

    def __repr__(self):
        return "vehicle(%d) x=%f,y=%f"%(self.id,self.x,self.y)

    def move(self):
        print("move,cx=%f,cy=%f,nx=%f,ny=%f"%(self.x,self.y,self.nLoc.x,self.nLoc.y))
        if self.arrived():
            self.destroy()
            return False
        if self.nLoc.x-1<=self.x <= self.nLoc.x+1 and self.nLoc.y-1<=self.y <= self.nLoc.y+1:
            self.jointCount = self.jointCount + 1
            self.cLoc = self.nLoc
            if self.jointCount == len(self.route.joints):
                print(self,"end")
                self.nLoc = self.route.end
            else:
                print(self,"jointCount: ",self.jointCount,"joints: ", len(self.route.joints))
                self.nLoc = self.route.joints[self.jointCount]
            self.__changeDirection()
            self.dx *= self.wr
            self.dy *= self.hr
        self.canvas.move(self.id, self.dx, self.dy)
        #self.canvas.move(self.text, self.dx, self.dy)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        #print("%s %d %d"%(self,self.x,self.y))
        return True

    def __changeDirection(self):
        direction = self.__calcDirection()
        self.dx, self.dy = 0, 0
        if direction == "north":
            self.dy = -50
            self.photo = self.picNorth
            self.offsetX = 9
            self.offsetY = 0
        elif direction == "south":
            self.dy = 50
            self.photo = self.picSouth
            self.offsetX = -9
            self.offsetY = 0
        elif direction == "east":
            self.dx = 50
            self.photo = self.picEast
            self.offsetY = 9
            self.offsetX = 0
        elif direction == "west":
            self.dx = -50
            self.photo = self.picWest
            self.offsetY = -9
            self.offsetX = 0
        
        if self.id is not None:
            self.canvas.itemconfigure(self.id, image=self.photo)
            self.canvas.coords(self.id, self.x + self.offsetX, self.y+self.offsetY)

    def __calcDirection(self):
        if self.nLoc.x-1 <= self.x <= self.nLoc.x+1:
            if self.cLoc.y < self.nLoc.y-1:
                return "south"
            else:
                return "north"
        elif self.x < self.nLoc.x-1:
            return "east"
        else:
            return "west"

    def destroy(self):
        #print("%s arrived"%self)
        self.canvas.delete(self.id)

    def arrived(self):
        return self.route.end.x-1 <= self.x <= self.route.end.x+1 and self.route.end.y-1 <= self.y <= self.route.end.y+1

    def __hash__(self):
        return self.id

    def __eq__(self,other):
        return self.id == other.id
