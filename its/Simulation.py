from tkinter import *
from Vehicle import Vehicle
from Controller import Controller

class Simulation(Frame):
    def __init__(self, root, config):
        Frame.__init__(self, root, height=500, width=500)
        self.grid(column=2,row=1, sticky=N+E+S+W)

        self.initWidgets()
        self.initEvents()
        self.initController(config)

    def initWidgets(self):
        self.btn = Button(self,text="Test")
        self.btn.grid(column=2, row=1)

        self.canvas = Canvas(self)
        self.canvas.grid(column=1, row=1)
#	self.canvas.pack(expand=YES, fill=BOTH)

        self.vehicle = Vehicle(1,"south")
        self.vehicle.draw(self.canvas)

	
    def initEvents(self):
        #for panel
        pass

    def initController(self, config):
        self.ctrl = Controller(config, self.canvas)

    def start(self):
        #while loop
        while True:
            #time.sleep a tick time might be couple milliseconds
            self.ctrl.tick()
            self.vehicle.move()
            #self.canvas.update()

def main():
    root = Tk()
    root.title("Intelligent Transportation Simulation")

    sm = Simulation(root,config="init.config")
    #sm.start()

    root.mainloop()

if __name__ == '__main__':
    main()
