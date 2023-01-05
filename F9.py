x = int(input("Adjon meg egy pozitív egész számot: "))
y = int(input("Adjon meg egy pozitív egész számot: "))

if x < y:
    for i in range(x+1,y,1):
        print(i)
elif x > y:
    for j in range(y+1,x,1):
        print(j)
else:
    print("A két szám megegyezik")