import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Teknőcök")

Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(4)
Sanyi.pencolor("Yellow")


for szog in [45, 90, 45, 90, 0]:
    Sanyi.forward(50)
    Sanyi.left(szog)

Sanyi.forward(25)

ablak.mainloop()