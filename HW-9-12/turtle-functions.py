import turtle

def hexagon(t,x,y,width,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(width)
    t.color(color)
    t.pendown()
    for t in range(6):
        t.forward(sidelen)
        t.right(60)

dora = turtle.Turtle()
print(hexagon(dora,0,0,2,"lightblue",50))

def ngon(t,numsides,x,y,color,width,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(width)
    t.color(color)
    t.pendown()
    for t in range(numsides):
        t.forward(sidelen)
        t.right(360/numsides)

      
paula = turtle.Turtle()
print(ngon(paula,12,0,0,5,"pink",30))

wn = turtle.Screen 
wn.exitonclick()
wn.mainloop()

# position turtle (set postion (x,y) by typing: posiyion_turtle)
