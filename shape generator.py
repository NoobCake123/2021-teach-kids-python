import turtle

t=turtle.pen
a=input("side length")
b=input("amount of sides")
for x in range(b):
    t.forward(a)
    t.left(b*180-360)