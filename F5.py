x = int(input("Adjon meg egy számot: "))
y = int(input("Adjon meg egy számot: "))
z = int(input("Adjon meg egy számot: "))

if x + y == z:
    print("x és y összege megegyezik z értékével")
elif x + z == y:
    print("x és z összege megegyezik y értékével")
elif y + z == x:
    print("y és z összege megegyezik x értékével")
else:
    print("Egyik számpár összege sem egyenlő a harmadik értékével")