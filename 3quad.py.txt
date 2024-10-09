import turtle
def dq1 (t,cor,lado,ang):
    t.fillcolor(cor)
    t.begin_fill()
    t.fd(lado)
    t.left(ang)
    t.fd(lado)
    t.left(ang)
    t.fd(lado)
    t.left(ang)
    t.fd(lado)
    t.left(ang)
    t.end_fill()
    return

def w1(t,lado,lado2,ang):
    t.up()
    t.fd(lado)
    t.left(ang)
    t.fd(lado2)
    t.right(ang)
    t.down()
    return
def w2(t,lado,lado2,ang):
    t.up()
    t.fd(lado)
    t.left(ang)
    t.fd(lado2)
    t.right(ang)
    t.down()
    return
t=turtle.Turtle()
dq1(t,"red",100,90)
w1(t,100,50,90)
dq1(t,"black",50,90)
w2(t,50,25,90)
dq1(t,"green",25,90)
