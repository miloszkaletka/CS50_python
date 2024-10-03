def main():
    GroceryList = {}

    while True:
        try:
            # .strip() usuwa białe znaki z początku i końca wprowadzonego tekstu (np. spacje).
            item = input().strip().lower()
        except EOFError:
            break

        if item not in GroceryList:
            GroceryList[item] = 1
        else:
            GroceryList[item] += 1

    for item in sorted(GroceryList):  # sortuje A-Z
        # Wypisuje ilosc produktow a  funkcja upper zapisuje slowa wielkimi literami
        print(f"{GroceryList[item]} {item.upper()}")


if __name__ == "__main__":
    main()
