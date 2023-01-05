szo = input("Adjon meg egy stringet: ")

hossz = []
def csillag():
    for i in szo:
        hossz.append(i)
    print(szo)
    print(len(hossz)*"*")


csillag()