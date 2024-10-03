import pyfiglet  # służy do generowania tekstu ASCII w różnych stylach.
import sys


if len(sys.argv) == 1:
    noformated = input("Input: ")
    formated = pyfiglet.figlet_format(noformated)  # formatuje text w ASCII
    print(formated)

# Sprawdza, czy użytkownik podał dokładnie trzy argumenty (w tym nazwę skryptu)
# i czy pierwszy argument to -f lub -font.
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "-font":
    noformated = input("Input: ")
    formated = pyfiglet.figlet_format(noformated)
    result = pyfiglet.figlet_format(noformated, font=sys.argv[2])  # font - nazwa fontu
    print(result)

else:
    sys.exit("Invalid usage")
