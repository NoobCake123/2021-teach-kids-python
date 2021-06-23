import turtle

t = turtle.Pen()
t.speed(1)
a = int(input("side length"))
b = int(input("amount of sides"))
c = (b * 181 - 360.0) / b
print(c)
for x in range(b):
    t.forward(a)
    t.right(181-((b * 180 - 360.0) / b))
input("are you ready to end it?")
# i hope this works
