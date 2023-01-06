szamok = []
szamok_hossza = 1000

for i in range(szamok_hossza):
    if i % 3 == 0 and len(szamok) < 100 and i != 0:
        szamok.append(i)

with open ("szamok.txt", "w") as file:
    for j in szamok:
        file.write(str(j))
        file.write('\n')


print(szamok)


