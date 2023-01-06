szovegfajl = open("temp.txt", "w")
szovegfajl.write("Debrecen")
szovegfajl.close()


szovegfajl = open("temp.txt","r")
print(szovegfajl.read())

word = "Debrecen"
with open("temp.txt","r") as fp:
    lines = fp.readlines()
    for line in lines:
        if line.find(word) != -1:
            print(word, "string megtalálható a fájlban")
        else:
            print(word, "string nem található meg a fileban")