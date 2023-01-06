import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Teknőcök")

Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.pensize(4)
Sanyi.pencolor("Yellow")

def haromszog():
    Sanyi.pencolor("black")
    for i in range(3):
        Sanyi.forward(50)
        Sanyi.left(120)

def negyszog():
    Sanyi.pencolor("Grey")
    for i in range(4):
        Sanyi.forward(50)
        Sanyi.left(90)

def otszog():
    Sanyi.pencolor("Blue")
    for i in range(5):
        Sanyi.forward(50)
        Sanyi.left(72)

def hatszog():
    Sanyi.pencolor("Red")
    for i in range(6):
        Sanyi.forward(50)
        Sanyi.left(60)

def hetszog():
    Sanyi.pencolor("Darkgreen")
    for i in range(7):
        Sanyi.forward(50)
        Sanyi.left(51)

def nyolcszog():
    Sanyi.pencolor("purple")
    for i in range(8):
        Sanyi.forward(50)
        Sanyi.left(45)

def kilencszog():
    Sanyi.pencolor("yellow")
    for i in range(9):
        Sanyi.forward(50)
        Sanyi.left(40)

ablak.onkey(haromszog, 3)
ablak.onkey(negyszog, 4)
ablak.onkey(otszog, 5)
ablak.onkey(hatszog, 6)
ablak.onkey(hetszog, 7)
ablak.onkey(nyolcszog, 8)
ablak.onkey(kilencszog, 9)

ablak.listen()
ablak.mainloop()
