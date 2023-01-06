szo = input("Adjon meg egy stringet: ")

RSV = []
def forditott():
    for i in szo:
        RSV.append(i)

    RSV.reverse()
    print(RSV)

forditott()