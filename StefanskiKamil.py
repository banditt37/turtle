import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(20)

def base():
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

def cross(x, y, outline, fill, fds, fdl, rt, lt):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for i in range(4):
        t.fd(fds)
        t.rt(rt)
        t.fd(fdl)
        t.lt(lt)
        t.fd(fdl)
        t.rt(rt)
        t.fd(fds)
    t.end_fill()
    t.penup()

def semicircle(x, y):
    turtle.circle(x, y)

base()
square(-500, -500, "black", "grey", 90, 1000)
square(140, -400, "black", "white", 90, 100)
square(-200, -50, "black", "lightblue", 90, 120)
square(50, -50, "black", "lightblue", 90, 120)
right(-250, 0, "black", "black", 500, 135, 705)
square(-200, 100, "black", "lightblue", 90, 120)
right(-225, -500, "black", "green", 25, 135, 35.25)
right(-200, -500, "black", "red", 25, 135, 35.25)
right(-200, -500, "black", "blue", 25, 135, 35.25)
right(-175, -500, "black", "orange", 25, 135, 35.25)
cross(220, -460, "black", "grey", 5, 10, 90, 90)
cross(-140, -170, "black", "yellow", 5, 55, 90, 90)
cross(-140, 100, "black", "yellow", 5, 55, 90, 90)
cross(110, -170, "black", "yellow", 5, 55, 90, 90)
semicircle(100,180)