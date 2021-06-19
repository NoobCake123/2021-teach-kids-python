import _random
import random
import turtle
import time
t = turtle.Pen
e = turtle.textinput("What is your name?", "enter name here:")
colors = ["red", "blue"]
f = input("would you like to stop looking at alllllllll the spirals? Yes for Yes, or No for no. if you don't say yes or no, you will be in quite for a surprise.")

print(f)

if f == ("yes" or "Yes"):
    pass
elif f == ("no" or "No"):
    print("Ok. Just to trigger you, it's over.")
    print("JUST KIDDING I WOULDNT DO THAT HERES 30 SECONDS")
    time.sleep(30)
else:
    turtle.clear()
    for x in range(25):
        t.setx(random.randint(-250, 250))
        t.sety(random.randint(-250, 250))
        t.penup()
        b = random.choice(colors)
        t.color(b)
        t.pendown()
        t.write(e, "sucks")
    time.sleep(120)