'''
Created on Feb 1, 2012

@author: jiayu
'''
from tkinter import *
from its.core.Test import ATest

def readFile(file_name):
    roads = []
    in_file = open(file_name, "r")
    for line in in_file:
        line = line.strip("\n")
        line_split = line.split()
        a_road = []
        for i in line_split:
            a_road.append(i)
        roads.append(a_road)
    in_file.close()
    return roads


if __name__ == '__main__':
    draw_coords = readFile("param.txt")
    
    root = Tk()
    canvas = Canvas(root, width=200, height=100)
    canvas.pack()
    
    for line_coord in draw_coords:
        canvas.create_line(line_coord,fill="#D186A4",width=10)
    root.mainloop()
