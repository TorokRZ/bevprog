x = int(input("Adjon meg egy pozitív egész számot: "))
y = int(input("Adjon meg egy pozitív egész számot: "))
z = int(input("Adjon meg egy pozitív egész számot: "))

def PSTV():
    if (x and y and z) >= 0:
        return True
    else:
        return False

print(PSTV())