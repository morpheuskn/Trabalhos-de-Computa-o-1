import turtle
def dq1 (t):
    t.fillcolor("red")
    t.begin_fill()
    t.left(45)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(45)
    t.end_fill()
    return

def dq2 (a):
    a.fillcolor("black")
    a.begin_fill()
    a.left(45)
    a.fd(100)
    a.left(90)
    a.fd(100)
    a.left(90)
    a.fd(100)
    a.left(90)
    a.fd(100)
    a.left(45)
    a.end_fill()
    return

def w1(a):
    a.up()
    a.fd(100)
    a.down()
    return
def w2(t):
    t.up()
    t.fd(100)
    t.down()
    return
t=turtle.Turtle()
a=turtle.Turtle()
dq1(t)
w1(a)
dq2(a)
