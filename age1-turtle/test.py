import _random
import turtle
import random
t = turtle.Pen()
t.speed(0)
colors = ["red","orange","yellow","green","blue","violet","purple"]
for x in range(360):
      a = random.choice(colors)
      t.color(a)
      t.circle(100+x)
      t.left(1)
input("are you ready to stop starin @ ur creation?")




