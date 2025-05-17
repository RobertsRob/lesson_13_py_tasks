# 1.task
# Нарисуй простой дом с квадратом (стены) и треугольником (крыша). Можно добавить детали: окно или дверь.
import turtle

t = turtle.Turtle()

# Стены
t.penup()
t.goto(-50, -50)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.left(90)

# Крыша
t.goto(-50, 50)
t.goto(0, 100)
t.goto(50, 50)
t.goto(-50, 50)

# Дверь
t.penup()
t.goto(-10, -50)
t.pendown()

for _ in range(2):
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)

t.hideturtle()
turtle.done()

# 2.task
# Попроси пользователя ввести количество лучей, затем построй симметричную звезду с этим числом.
import turtle

t = turtle.Turtle()
t.speed(0)

n = int(input("Введите количество лучей: "))

for _ in range(n):
    t.forward(100)
    t.backward(100)
    t.right(360 / n)

turtle.done()

# 3.task
# С помощью turtle напиши своё имя по буквам. Используй команды penup(), pendown(), goto() и линии для построения каждой буквы.
# 4.task

# 5.task

# 6.task
