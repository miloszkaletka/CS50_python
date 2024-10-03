def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")  # .2f - wyswietla 2 miejsca po przecinku


def dollars_to_float(d):  # usuwa $ z inputu uzytkownika i zmienia na float
    d = d.replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):  # usuwa % z inputu uzytkownika i zmiania na float
    p = p.replace("%", "")
    p = float(p) / 100
    return p


main()
