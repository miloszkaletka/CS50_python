while (
    True
):  # program dziala nieskonczonosc dopoki nie napotka break lub wile zmieni sie na False
    try:  # umieszczamy tu kod ktory moze potencjalnie wywolac error

        x, y = input("Fraction: ").split(
            "/"
        )  # uzytkownik musi wprowadzic liczby w formacie 3/4

        x = int(x)
        y = int(y)

        if x / y > 1:  # paliwa nie moze byc wiecej niz pojemnosc zbiornika
            print("")
            continue

        percentage = f"{x/y:.0%}"  # do wyniku dodajemy%
        if percentage == "0%" or percentage == "1%":
            print("E")
        elif percentage == "100%" or percentage == "99%":
            print("F")

        else:
            print(percentage)

    except ValueError:
        print("")

    except ZeroDivisionError:
        print("")

    else:
        break
