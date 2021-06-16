import turtle
t= turtle.Pen()
t.speed(0)
colors = ["red","yellow","blue","green"]
for x in range(360):
    t.pencolor(colors[2^x%4])
    t.circle(100)
    t.left(1)

