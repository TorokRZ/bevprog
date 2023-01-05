sor = int(input("Adjon meg egy pozitív egész számot: "))
oszlop = int(input("Adjon meg egy pozitív egész számot: "))

def FGV():
    for i in range(sor):
        for j in range(oszlop):
            print("*",end=' ')
        print()


FGV()