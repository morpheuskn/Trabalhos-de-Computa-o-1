import turtle
b=turtle.Turtle()
a=open("p:/misterio.dat","r")
b.hideturtle()
for linha in a:
    linha=linha.strip()
    if linha == "CIMA":
       b.up()
    elif linha == "BAIXO":
       b.down()
    else:
        d=linha.find(" ")
        x=int(linha[:d])
        y=int(linha[d:])
        b.goto(x,y)
a.close()
