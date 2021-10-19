import turtle
import math
wn = turtle.Screen()
pen = turtle.Turtle()
pen.left(90)
pen.speed(10)
arr = []

#vẽ cái thân
def drawLine(lowest,largest, constant):
    for i in range(2):
        arr.append(constant)
        pen.penup()
        pen.goto(lowest,constant)
        pen.color('red')
        for x in range (lowest, largest):
            pen.pendown()
            y=10*math.sin(3*math.radians(x)) + constant
            pen.goto(x,y)
            if x == largest-1:
                arr.append(x)
                arr.append(y)
                continue 
        constant = constant -10

#vẽ cái lưỡi
def drawTonge(smallest, biggest, cons):
    for i in range (smallest, biggest):
        pen.pendown()
        u=4*math.sin(10*math.radians(i))+ cons
        pen.goto(i,u)

#vẽ cái đầu
def drawcircle(r, l):
    pen.color("red", "red")
    pen.begin_fill()
    pen.right(120)
    for loop in range(l):
        pen.circle(r,90)
        pen.circle(r/2,90)
    # pen.circle(r,120)
    # pen.right(90)
    
    pen.end_fill()
    
def drawSnake(start, end, point):
    drawLine(start,end, point)
    print(arr)
    const = arr[0]-5
    x2 = arr[4]
    y2 = arr[5]
    startpoint = x2,y2
    pen.penup()
    pen.goto(startpoint)
    pen.pendown()
    drawcircle(20, 2)
    print(pen.xcor(), pen.ycor())
    newx = int(pen.xcor())
    drawTonge(newx, newx+50, const)
    
    # drawTonge(145, 180, 43)

drawSnake(-100, 100, 0)
pen.penup()
pen.home()
turtle.done()

