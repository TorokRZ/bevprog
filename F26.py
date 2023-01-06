with open("temp.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        if count % 2 == 0:
            print(line)