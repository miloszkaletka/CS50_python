food = {
    "Baja Taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00,
}

total = 0.0

while True:
    try:
        item = input("Item: ")
    except EOFError:  # jezli uzytkownik kliknie ctrl + d konczymy program
        break
    if item not in food:
        print(f"Total: ${total:.2f}")
        continue
    # jezeli przedmiot nie wystepuje na liscie to czekamy az podana zostanie inna wartosc

    if item in food:  # dodajemy cene produktu do ceny total i wracamy do poczatku
        price = food.get(item)
        total += price
        print(f"Total: ${total:.2f}")
