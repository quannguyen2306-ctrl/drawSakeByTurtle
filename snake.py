import turtle
import math
wn = turtle.Screen()
pen = turtle.Turtle()
pen.left(90)
pen.speed(10)
arr = []

#vẽ cái thân
def drawLine(lowest,largest, constant):
    pen.penup()
    pen.goto(lowest,constant)
    pen.color('red')
    for x in range (lowest, largest):
        pen.pendown()
        y=10*math.sin(5*math.radians(x)) + constant
        pen.goto(x,y)
        if x == largest-1:
            arr.append(x)
            arr.append(y)
            continue 

#vẽ cái lưỡi
def drawTonge(smallest, biggest, cons):
    for i in range (smallest, biggest):
        pen.pendown()
        u=4*math.sin(15*math.radians(i)) + cons
        pen.goto(i,u)

#vẽ cái đầu
def drawcircle(r):
    pen.color("red", "red")
    pen.begin_fill()
    pen.right(120)
    for loop in range(2):
        pen.circle(r,90)
        pen.circle(r/2,90)
    # pen.circle(r,120)
    # pen.right(90)
    pen.end_fill()
    
def drawSnake():
    
    drawLine(-150,125, 50)
    drawLine(-150,125, 40)
    print(arr)
    x1 = arr[0]
    y1 = arr[1]
    x2 = arr[2]
    y2 = arr[3]
    midpoint = x2,y2
    print(midpoint)
    pen.penup()
    pen.goto(midpoint)
    pen.pendown()
    drawcircle(20)
    pen.penup()
    pen.goto(x1,y1)
    drawTonge(125, 180, 43)

drawSnake()
pen.penup()
pen.home()
turtle.done()

