import random


def get_level():
#Pobiera poziom od użytkownika (1, 2 lub 3) i upewnia się, że jest on prawidłowy.
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n 
            else:
                print("Level: ")
        except ValueError:
            print("Podaj liczbę całkowitą (1, 2 lub 3).")


def main():
    # Liczba prób na jedno pytanie
    max_proby = 3

    liczba_pytan = 10

    # Pobiera poziom od użytkownika
    n = get_level()

    wynik = 0  # Liczba poprawnych odpowiedzi

    for _ in range(liczba_pytan): #wybieramy zakres dodawania
        if n == 1:
            number1 = random.randint(1, 10)
            number2 = random.randint(1, 10)
        elif n == 2:
            number1 = random.randint(10, 99)
            number2 = random.randint(10, 99)
        else:  # n == 3
            number1 = random.randint(100, 999)
            number2 = random.randint(100, 999)

        poprawny_wynik = number1 + number2

        # Zmienne do kontroli prób
        proby = max_proby
        while proby > 0:
            try:
                odpowiedz = int(input(f"{number1} + {number2} = "))
                if odpowiedz == poprawny_wynik:
                    wynik += 1
                    break
                else:
                    proby -= 1
                    print("EEE")
            except ValueError:
                print("EEE")
                proby -= 1

        # Jeśli użytkownik nie udzielił poprawnej odpowiedzi w 3 próbach, podaj prawidłowy wynik
        if proby == 0:
            print(f"{number1} + {number2} = {poprawny_wynik}")


if __name__ == "__main__":
    main()



