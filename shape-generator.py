import turtle

t = turtle.Pen()
t.speed(0)
a = int(input("side length"))
b = int(input("amount of sides"))
c = (b * 180 - 360.0) / b
print(c)
for x in range(b):
    t.forward(a)
    t.right(180-((b * 180 - 360.0) / b))
input("are you ready to end it?")
# i hope this works
