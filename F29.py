import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Teknőcök")

Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(4)
Sanyi.pencolor("Yellow")

for i in range(3):
    Sanyi.forward(30)
    Sanyi.left(120)

Sanyi.penup()
Sanyi.goto(50,50)
Sanyi.pendown()

for i in range(3):
    Sanyi.forward(40)
    Sanyi.left(120)

Sanyi.penup()
Sanyi.goto(100,100)
Sanyi.pendown()

for i in range(3):
    Sanyi.forward(50)
    Sanyi.left(120)

ablak.mainloop()
