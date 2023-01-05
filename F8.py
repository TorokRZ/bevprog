x = int(input("Adjon meg egy pozitív egész számot: "))
kisebb_szamok = []
oszthato_szamok = []

for i in range(x-1,0,-1):
    kisebb_szamok.append(i)

print(kisebb_szamok)

for j in kisebb_szamok:
    if j % 3 == 0:
      oszthato_szamok.append(j)

print(oszthato_szamok)