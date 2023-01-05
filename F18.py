x = int(input("Adjon meg egy pozitív egész számot: "))
y = int(input("Adjon meg egy pozitív egész számot: "))

osszeg = []
def intervallum():
    for i in range(x,y,1):
        osszeg.append(i)
    print(sum(osszeg))

intervallum()

