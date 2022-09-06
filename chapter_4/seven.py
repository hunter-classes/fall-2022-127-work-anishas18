import turtle
wn = turtle.Screen()
dp = turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    dp.left(angle)
    dp.forward(100)
print("The pirate's final heading was", dp.heading())
wn.exitonclick()