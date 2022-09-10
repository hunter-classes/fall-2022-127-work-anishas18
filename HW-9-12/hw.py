import turtle

def hexagon(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(6):
        t.forward(sidelen)
        t.right(60)

dora = turtle.Turtle()
hexagon(dora,0,0,2,"lightblue", 100)

def ngon(t,numsides,x,y,color,w,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(numsides):
        t.forward(sidelen)
        t.right(360/numsides)
paula = turtle.Turtle()
ngon(paula,12,0,0,5,"pink",30)

wn.exitonclick()
wn.mainloop()
