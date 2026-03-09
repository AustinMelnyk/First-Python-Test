from turtle import *

import random as r

x=1000
bgcolor("black") # Set background color
color("#ffec70") # Set line color
speed(0) #pen speed
#tracer(0) #turn off screen updating

circle(50)

penup()
pendown()

circle(5)
begin_fill()

while True:
   forward(r.randint(10,100))#move random
   right(90) #turn 90°
   x=x-5 #lets make it spiral
   if  x <1:
        #update() #update once at the end
        end_fill()
        done()
        break