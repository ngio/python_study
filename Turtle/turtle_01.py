# https://docs.python.org/ko/3/library/turtle.html#starting-a-turtle-environment

from turtle import *

forward(100)
left(120)
forward(100)

home()  # (0,0)
pos()
clearscreen()

color('red')
fillcolor('yellow')

begin_fill()

while True:
    forward(100)
    left(170)
    if abs(pos()) < 1:
        break;
    
end_fill()


