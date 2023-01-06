import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Teknőcök")

Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(4)
Sanyi.pencolor("Yellow")

for szog in range(5):
    Sanyi.forward(100)
    Sanyi.left(144)



ablak.mainloop()