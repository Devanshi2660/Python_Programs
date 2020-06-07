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
#x.circle(360)
drawSpecial(x,100,10,4)

def drawCircles(t,size,a):
    for i in range(4):
        t.circle(size)
        size=size-a
y = turtle.Turtle()
y.speed(0)
y.color('purple')
#y.circle(90)

drawSpecial(y,100,10,10)
z = turtle.Turtle()
z.speed(0)
z.color('blue')
#right=int(80)

drawSpecial(z,100,10,5)
a = turtle.Turtle()
a.speed(0)
a.color('green')
#right=int(90)

drawSpecial(a,100,10,19)
b = turtle.Turtle()
b.speed(0)
b.color('yellow')
#right=int(90)

drawSpecial(b,100,10,20)
turtle.done()
