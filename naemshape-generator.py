import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
sides = int(turtle.textinput("Enter your name", "how many sides?"))
your_name = turtle.textinput("Enter you name", "what is your name")
colors = ["red", "yellow", "blue", "green", "orange", "aqua"]
for x in range(sides):
    t.pencolor(colors[x % 6])
    t.penup()
    t.forward(20)
    t.pendown()
    t.write(your_name)
    t.left(180 - ((sides * 180 - 360.0) / sides))
input("do you want to stop staring at your creation?")
