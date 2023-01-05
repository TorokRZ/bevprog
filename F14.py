import math
x = float(input("Adjon meg egy pozitív valós számot: "))
y = float(input("Adjon meg egy pozitív nagyobb valós számot: "))

kerekitett1 = math.floor(x)
kerekitett2 = math.floor(y)

print(kerekitett1,kerekitett2)

for i in range(kerekitett1+1,kerekitett2,1):
    print(i)