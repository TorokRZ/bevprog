x = int(input("Adjon meg egy pozitív egész számot: "))

osszeadando = []
for i in range(x,0,-1):
    osszeadando.append(i)

print(osszeadando)
print(sum(osszeadando))