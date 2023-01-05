x = int(input("Adjon meg egy pozitív egész számot: "))

tarolo = []
def FNC():
    for i in range(x):
        tarolo.append(i)
        if len(tarolo) % 3 == 0:
            print("+")
        else:
            print("-")

FNC()