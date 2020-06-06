import turtle
import math
import random
def drawCircles(t,size):
    def drawSpecial(t,size,repeat):
        wn = turtle.Screen()
        wn.bgcolor('black')
        x = turtle.Turtle()
        x.speed(0)
        x.color('red')
        #rotate=int(360) 

        drawCircles(t,size)
        for i in range(10):
            t.circle(size)
            size=size-4
            
        drawSpecial(t,size,repeat)
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
        drawSpecial(x,100,10)
        y = turtle.Turtle()
        y.speed(0)
        y.color('purple')
        #rotate=int(90)
        drawCircles(t,size)
        for i in range(4):
            t.circle(size)
            size=size-10
        drawSpecial(t,size,repeat)
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
        drawSpecial(y,100,10)
        z = turtle.Turtle()
        z.speed(0)
        z.color('blue')
        #rotate=int(80)
        drawCircles(t,size)
        for i in range(4):
            t.circle(size)
            size=size-5
        drawSpecial(t,size,repeat)
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
        drawSpecial(z,100,10)
        a = turtle.Turtle()
        a.speed(0)
        a.color('green')
        #rotate=int(90)
        drawCircles(t,size)
        for i in range(4):
            t.circle(size)
            size=size-19
        drawSpecial(t,size,repeat)
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
        drawSpecial(a,100,10)
        b = turtle.Turtle()
        b.speed(0)
        b.color('yellow')
        #rotate=int(90)
        drawCircles(t,size)
        for i in range(4):
            t.circle(size)
            size=size-20
        drawSpecial(t,size,repeat)
        for i in range (repeat):
            drawCircles(t,size)
            t.right(360/repeat)
            drawSpecial(b,100,10)
turtle.done()