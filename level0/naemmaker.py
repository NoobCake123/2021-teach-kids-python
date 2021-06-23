import turtle

t = turtle.Pen()
t.speed(0.5)
turtle.bgcolor("black")
your_name = turtle.textinput("Enter you name", "what is your name")
colors = ["red", "yellow", "blue", "green", "orange", "aqua"]
for x in range(100):
    t.pencolor(colors[x % 6])
    t.penup()
    t.forward((x * 6))
    t.pendown()
    t.write(your_name, font=("Times", int(x + 6 / 6), "bold"))
    t.left(63)
input("are you ready to stop looking at your creation?")
