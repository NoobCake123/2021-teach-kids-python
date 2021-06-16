import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.color("red")
circlus = int(turtle.numinput("number of circles", "how many circles do you want on your rosette?"))
radius = int(turtle.numinput("radius", "radius"))
thiccness = int(turtle.numinput("how dummi thicc do you want it 2 be?", "how thicc"))
for x in range(circlus):
    t.width(thiccness)
    t.circle(radius)
    t.left(360/circlus)
input("are you ready to end your creation?")
