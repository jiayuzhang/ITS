from tkinter import *
#from threading import *
import threading
from Vehicle import Vehicle
from Controller import Controller
from Point import Point
from Route import Route
import time

class Simulation(Frame):
    def __init__(self, root, config):
        Frame.__init__(self, root)
        self.grid(column=3,row=2, sticky=N+E+S+W)
        self.stopped = True
        self.started = False
        
        self.initWidgets()
        self.initEvents()
        self.initController(config)

    def initWidgets(self):
        self.startBtn = Button(self,text="Start")
        self.startBtn.grid(column=1, row=1)

        self.stopBtn = Button(self,text="Stop")
        self.stopBtn.grid(column=2, row=1)
        self.stopBtn['state'] = "disabled"

        self.stepBtn = Button(self,text="Step")
        self.stepBtn.grid(column=3, row=1)

        self.canvas = Canvas(self, height=700, width=900)
        self.canvas.grid(row=2, column=1, columnspan=3)
        
        #r = Route(Point(100, 300, self.canvas), Point(300,500,self.canvas), [Point(300,300, self.canvas)])
        #self.vehicle = Vehicle(1,r,self.canvas)
        #self.vehicle.create()

    def startPressed(self, event):
        print("start click", threading.currentThread)
        if not self.started:
            self.toggleBtn(self.stopBtn)
            self.toggleState()
            self.started = True
            self.start()
        else:
            self.toggleState()
            if not self.stopped:
                self.start()
        
    def stopPressed(self, event):
        self.resetState()
        self.resetBtns()
        #self.ctrl.reset()

    def stepPressed(self, event):
        self.start()
        pass

    def resetBtns(self):
        self.startBtn['text']= "Start"
        self.stopBtn['state'] = "disabled"

    def resetState(self):
        self.started = False
        self.stopped = True

    def toggleBtn(self, btn):
        if btn['state'] == "disabled":
            btn['state'] = "normal"
        else:
            btn['state'] = "disabled"

    def toggleState(self):
        if not self.stopped:
            self.startBtn["text"] = "Resume"
            self.stopped = True
        else:
            self.startBtn["text"] = "Pause"
            self.stopped = False
            
    def initEvents(self):
        self.startBtn.bind("<Button-1>", self.startPressed)
        self.stopBtn.bind("<Button-1>", self.stopPressed)
        self.stepBtn.bind("<Button-1>", self.stepPressed)

    def initController(self, config):
        self.ctrl = Controller(config, self.canvas)

    def start(self):
        #while loop
        while True:
            #time.sleep a tick time might be couple milliseconds
            self.ctrl.tick()
            #self.vehicle.move()
            self.canvas.update()
            time.sleep(0.05)
            if self.stopped:
                break

def main():
    root = Tk()
    root.title("Intelligent Transportation Simulation")
    sm = Simulation(root, config="init.config")

    #sm.start()

    root.mainloop()

if __name__ == '__main__':
    main()
