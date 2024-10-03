import sys
import csv  # odczyt i zapis plikow csv

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    try:  # otwieramy 2 pliki argv1 do odczytu i argv2 do zapisu
        with open(sys.argv[1], "r") as rfile, open(sys.argv[2], "w") as wfile:
            reader = csv.DictReader(
                rfile
            )  # tworzymy obiekt ktory czyta plik jak slownik/dict
            for row in reader:  # dla kazdego wersu w pliku
                splited = row["name"].split(
                    ","
                )  # podziel kolumne name na imie i nazwisko za pomoca przecninka
                students.append(  # dodajemy do listy slownik z kluczami first last house
                    {
                        "first": splited[1].lstrip(),
                        "last": splited[0],
                        "house": row["house"],
                    }
                )  # tworzymy plik writer ktory zapisuje do nowego pliku csv
            writer = csv.DictWriter(wfile, fieldnames=["first", "last", "house"])
            writer.writerow(
                {"first": "first", "last": "last", "house": "house"}
            )  # zapisuje 1 wiersz naglowkami z kolumn
            for row in students:
                writer.writerow(  # zapisujemy kazdy wiersz z listy students do nowego csv
                    {"first": row["first"], "last": row["last"], "house": row["house"]}
                )

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
