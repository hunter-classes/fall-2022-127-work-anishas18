import turtle
    
def square(t,x,y,w,color,sidelen):
    # set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    
  # draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)

def triangle(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.right(120)

alex = turtle.Turtle()
triangle(alex, 0,0, 5, "blue", 100)

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



wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)

wn.exitonclick()
wn.mainloop()
