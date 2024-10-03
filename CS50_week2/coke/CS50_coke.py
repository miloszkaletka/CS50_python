i = 50


while i > 0:
    x = int(input("Insert Coin: "))
    if x == 5 or x == 10 or x == 25:
        i = i - x

        if i > 0:
            print("Amount Due: ", i)

        elif i == 0:
            print("Change Owed: 0")

        elif i < 0:
            print("Change Owed: ", abs(i))  # oznacza wartosc bezwzgledna

    else:
        print("Amount Due: ", i)
