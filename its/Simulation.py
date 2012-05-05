from tkinter import *
#from threading import *
import threading
from Vehicle import Vehicle
from Controller import Controller
import time

class Simulation(Frame):
    def __init__(self, root, config):
        Frame.__init__(self, root, height=700, width=900)
        self.grid(column=3,row=2, sticky=N+E+S+W)
        self.status = "stop"
     
        self.initWidgets()
        self.initEvents()
        self.initController(config)

    def initWidgets(self):
        self.startBtn = Button(self,text="Start")
        self.startBtn.grid(column=1, row=1)

        self.stopBtn = Button(self,text="Stop")
        self.stopBtn.grid(column=2, row=1)

        self.stepBtn = Button(self,text="Step")
        self.stepBtn.grid(column=3, row=1)

        self.canvas = Canvas(self)
        self.canvas.grid(row=2, column=1, columnspan=3)

        self.vehicle = Vehicle(1,"south",self.canvas)
        self.vehicle.create()

    def startPressed(self, event):
        print("start click", threading.currentThread)
        if self.status == "stop":
            self.status = "start"
            self.startBtn["text"] = "Pause"
            self.start()
        elif self.status == "start":
            self.status = "pause"
            self.startBtn["text"] = "Resume"
        elif self.status == "pause":
            self.status = "start"
            self.startBtn["text"] = "Pause"
            
    def stopPressed(self, event):
        self.status = "stop"
        pass

    def stepPressed(self, event):
        self.status = "step"
        pass

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
            self.vehicle.move()
            time.sleep(0.1)
            self.canvas.update()

def main():
    root = Tk()
    root.title("Intelligent Transportation Simulation")
    sm = Simulation(root, config="init.config")
    #sm.start()

    root.mainloop()

if __name__ == '__main__':
    main()
