import turtle
import math
import random

def drawCircles(t,size,a):
    for i in range(10):
        t.circle(size)
        size=size-a
        
def drawSpecial(t,size,repeat,a):
  for i in range (repeat):
    drawCircles(t,size,a)
    t.right(360/repeat)

wn = turtle.Screen()
wn.bgcolor('black')
x = turtle.Turtle()
x.speed(0)
x.color('red')

drawSpecial(x,100,10,4)

def drawCircles(t,size,a):
    for i in range(4):
        t.circle(size)
        size=size-a
y = turtle.Turtle()
y.speed(0)
y.color('purple')


drawSpecial(y,100,10,10)
z = turtle.Turtle()
z.speed(0)
z.color('blue')


drawSpecial(z,100,10,5)
a = turtle.Turtle()
a.speed(0)
a.color('green')


drawSpecial(a,100,10,19)
b = turtle.Turtle()
b.speed(0)
b.color('yellow')


drawSpecial(b,100,10,20)
turtle.done()
