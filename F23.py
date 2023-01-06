szamok = []

while True:
    x = int(input("Adjon meg egy pozitív egész számot: "))
    if x != 0:
        szamok.append(x)
    else:
        print("Nullát adott meg értéknek")
        break
szamok.reverse()

print(szamok)