import turtle
t = turtle.Pen()
t.shape("circle")

def Move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def Rectangle(range=60):
    t.pendown()
    t.fd(range)
    t.lt(90)
    t.fd(range)
    t.lt(90)
    t.fd(range)
    t.lt(90)
    t.fd(range)
    t.penup()

def Triangle(range=60):
    t.pendown()
    t.fd(range)
    t.lt(120)
    t.fd(range)
    t.lt(120)
    t.fd(range)
    t.penup()

def Circle(size=30):
    t.pendown()
    t.circle(size)
    t.penup()

round = 1
xStart = -100
yStart = 200
while round <=4 :
    Move(xStart,yStart)
    Circle()
    t.fd(40)
    Rectangle()
    t.lt(90)
    t.fd(70)
    Triangle()
    t.lt(120)
    round += 1
    yStart -= 100
    
