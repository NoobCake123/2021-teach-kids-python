import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
your_name = turtle.textinput("Enter you name", "what is your name")
colors = ["red", "yellow", "blue", "green", "orange", "aqua"]
for x in range(420):
    t.pencolor(colors[x % 6])
    t.penup()
    t.forward(x * 3.6)
    t.pendown()
    t.write(your_name)
    t.left(69)
