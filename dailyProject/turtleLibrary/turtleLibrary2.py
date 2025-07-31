import turtle as t
import random

t.speed(0)
t.shape("turtle")

t.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(300):
    t.penup() # 펜을 올리고
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y) # 좌표로 이동
    
    c = random.choice(colors)
    t.color(c)
    
    t.pendown() # 펜을 내리고
    draw = random.choice([t.circle, t.dot]) # 원 또는 점 중 하나를 선택
    size = random.randint(1, 100) 
    draw(size) # 원 또는 점 그리기
t.done()
