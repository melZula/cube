#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
from tkinter import *
import numpy as np

master = Tk()

w = Canvas(master, width=500, height=500)	#initialization canvas
w.pack()

dots = [    np.array([[-50], [50], [-50],]),	#basic positions of dots
            np.array([[50], [50], [-50],]),
            np.array([[50], [-50], [-50],]),
            np.array([[-50], [-50], [-50],]),
            
            np.array([[-50], [50], [50],]),
            np.array([[50], [50], [50],]),
            np.array([[50], [-50], [50],]),
            np.array([[-50], [-50], [50],]),
            ]
    
alfa_xy = math.pi * 45 / 180  		# angle = 45 deg
alfa_yz = math.asin(math.sqrt(1/3))     #0.61547970867038734106746458912399
alfa_zx = 0.00


rot_matrix_z = np.array(  [ [math.cos(alfa_xy), -math.sin(alfa_xy), 0],  # rotation matrix for z
                            [math.sin(alfa_xy), math.cos(alfa_xy), 0],
                          [0, 0, 1] ]  )

rot_matrix_x = np.array(  [ [1, 0, 0],
                            [0, math.cos(alfa_yz), -math.sin(alfa_yz)],	 # rotation matrix for x
                          [0, math.sin(alfa_yz), math.cos(alfa_yz)] ]  )

new_dots=[]
for dot in dots: 
    dot_new = np.dot(rot_matrix_z, dot)
    dot_new = np.dot(rot_matrix_x, dot_new)
    new_dots.append(dot_new)
    
dots = new_dots


def draw_line(from_x, from_y, to_x, to_y):
    w.create_line(20,250,480,250,  arrow=LAST, arrowshape=(8,10,3), fill='blue')
    w.create_line(250,480,250,500-480,  arrow=LAST, arrowshape=(8,10,3), fill='blue')
    
    w.create_line(250+from_x, 250-from_y,
                  250+to_x,   250-to_y)

def main():
    global dots, w, alfa_zx

    w.delete('all')
    

    rot_matrix_y = np.array(  [ [math.cos(alfa_zx), 0, math.sin(alfa_zx)],
                                [0, 1, 0],
                              [-math.sin(alfa_zx), 0, math.cos(alfa_zx)] ]  )
                              
    new_dots=[]
    for dot in dots: 
        new_dot = np.dot(rot_matrix_y, dot)
        new_dots.append(new_dot)

    lines = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7),] #order of dots connection
    for line in lines:
        draw_line(new_dots[line[0]][0][0], new_dots[line[0]][1][0],	#drawing lines
                  new_dots[line[1]][0][0], new_dots[line[1]][1][0])

    alfa_zx += 0.01
    # вызываем саму себя каждые 30 миллисекунд
    master.after(30, main)


main()
master.mainloop()
