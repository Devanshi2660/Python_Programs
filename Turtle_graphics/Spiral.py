import turtle

spiral = turtle.Turtle()
spiral.getscreen().bgcolor("black")
spiral.color("white")
spiral.speed(30)
for i in range(33):
    spiral.circle(10*i)
    spiral.circle(-10*i)
    spiral.left(i)


turtle.done()