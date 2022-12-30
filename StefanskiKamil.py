import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(20)

def podstawa():
    t.penup()
    t.goto(-250, 0)
    t.pendown()
    t.color("black", "brown")
    t.begin_fill()
    for i in range(3):
        t.fd(500)
        t.rt(90)
    t.fd(500)
    t.end_fill()
    t.penup()

def square(x, y, outline, fill, rt, fd):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for i in range(4):
        t.rt(rt)
        t.fd(fd)
    t.end_fill()
    t.penup()

def right(x, y, outline, fill, fd, rt, fdl):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    t.fd(fd)
    t.rt(rt)
    t.fd(fdl)
    t.rt(rt)
    t.fd(fd)
    t.end_fill()
    t.penup()

def cross1():
    t.penup()
    t.goto(220, -460)
    t.pendown()
    t.color("black", "grey")
    t.begin_fill()
    for i in range(4):
        t.fd(5)
        t.rt(90)
        t.fd(10)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.fd(5)
    t.end_fill()
    t.penup()

def cross2():
    t.penup()
    t.goto(-140, -170)
    t.pendown()
    t.color("black", "yellow")
    t.begin_fill()
    for i in range(4):
        t.fd(5)
        t.rt(90)
        t.fd(55)
        t.lt(90)
        t.fd(55)
        t.rt(90)
        t.fd(5)
    t.end_fill()
    t.penup()

podstawa()
square(-500, -500, "black", "grey", 90, 1000)
square(140, -400, "black", "white", 90, 100)
square(-200, -50, "black", "lightblue", 90, 120)
right(-250, 0, "black", "black", 500, 135, 705)
right(-225, -500, "black", "green", 25, 135, 35.25)
right(-200, -500, "black", "red", 25, 135, 35.25)
right(-200, -500, "black", "blue", 25, 135, 35.25)
right(-175, -500, "black", "orange", 25, 135, 35.25)
cross1()
cross2()