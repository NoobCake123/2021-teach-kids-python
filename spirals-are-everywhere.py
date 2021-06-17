import _random
import random
import turtle

t = turtle.Pen()
turtle.screensize(800,800)
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple","gray","white"]
turtle.bgcolor("black")
for x in range(25):
    t.penup()
    t.setx(random.randint(-250, 250))
    t.sety(random.randint(-250, 250))
    b = random.choice(colors)
    a = random.randint(1, 5)
    d = random.randint(3,11)
    c = random.randint(1,3)
    if d == 11:
        t.color(b)
        t.pendown
        t.circle(a)
        t.left(36)
    else:
        for y in range(3*d):
            t.color(b)
            t.pendown()
            t.forward(a + ((11 - d)*y)/3)
            t.left((360/d)+c)
