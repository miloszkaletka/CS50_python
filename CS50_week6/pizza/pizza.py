import sys
import tabulate  # formatuje plik csv w postaci tableki
import os  # pozwala uzyc funkcji do sprawdzenia czy plik istnieje
import csv  # umozliwia czytanie i zapistywanie plikow csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")

elif os.path.splitext(sys.argv[1])[1] != ".csv":
    sys.exit("Not a CSV file")

elif os.path.isfile(sys.argv[1]) != True:
    sys.exit("File does not exist")

elif os.path.isfile(sys.argv[1]) == True:
    with open(
        sys.argv[1]
    ) as csv_file:  # otwieramy plik o nazwie 1 argumentu (with automatycznie po zamknieciu pliku zapisuje go)
        reader = csv.reader(
            csv_file
        )  # pozwala na odczytanie csv w postali listy wierszy
        rows = [
            row for row in reader
        ]  # Przekształca obiekt reader na listę wierszy z pliku CSV.
        print(tabulate.tabulate(rows, aheaders="firstrow", tablefmt="grid"))

        # uzywamy funkcji tabulate do wyswietlania tabeli,
        # headers= firstrow > uzywa pierwszego wiersza jako naglowka
        # rodzaj i format tabeli
