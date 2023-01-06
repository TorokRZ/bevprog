while True:
    x = int(input("adjon egy 20-nál kisebb számot: "))
    if 0 <= x <= 20:
        y = (x) * " "
        print(y+ "start")
        break
    else:
        print("adjon meg egy helyes számot")