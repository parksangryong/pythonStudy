import turtle as t
import random



def polygon(n):
    for i in range(n):
        t.fd(100)
        t.lt(360/n)

# 각 숫자별 polygon 함수들
def polygon1():
    polygon(1)

def polygon2():
    polygon(2)
    
def polygon3():
    polygon(3)
    
def polygon4():
    polygon(4)
    
def polygon5():
    polygon(5)
    
def polygon6():
    polygon(6)
    
def polygon7():
    polygon(7)
    
def polygon8():
    polygon(8)
    
def polygon9():
    polygon(9)

def go_right():
    t.setheading(0)
    t.fd(10)

def go_left():
    t.setheading(180)
    t.fd(10)

def go_up():
    t.setheading(90)
    t.fd(10)

def go_down():
    t.setheading(270)
    t.fd(10)

def pen_updown():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]
    random_color = random.choice(colors)
    t.pencolor(random_color)
    t.fillcolor(random_color)

def background_color():
    colors = ["white", "gray", "black"]
    random_color = random.choice(colors)
    t.bgcolor(random_color)

def clear():
    t.clear()
    t.pencolor('black')
    t.fillcolor('black')
    t.bgcolor('white')


pen_size = 1

def pen_size_up():
    global pen_size
    print(f"pen_size_up: {pen_size}")
    if pen_size < 10:
        pen_size += 1
    t.pensize(pen_size)

def pen_size_down():
    global pen_size
    print(f"pen_size_down: {pen_size}")
    if pen_size > 1:
        pen_size -= 1
    t.pensize(pen_size)

