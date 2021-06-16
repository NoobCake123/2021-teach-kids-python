import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.color("red")
circlus = int(turtle.numinput("number of circles", "how many circles do you want on your rosette?"))
radius = int(turtle.numinput("radius", "radius"))
for x in range(circlus):
    t.circle(radius)
    t.left(360/circlus)
input("are you ready to end your creation?")
