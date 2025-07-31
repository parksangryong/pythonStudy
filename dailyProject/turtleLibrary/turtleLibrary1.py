import turtle as t
import random

t.speed(0)
t.shape("turtle")

t.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


i = 0
while True:
    t.color(random.choice(colors))
    t.fd(i)
    t.lt(200)
    i += 1