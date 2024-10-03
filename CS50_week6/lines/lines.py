#program liczy wiersze ktore maja kod bez pustych wierszy i komentarzy
import sys
import os

# sprawdzamy liczbe argumentow
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
# sprawdzamy czy plik ma istnieje
elif os.path.isfile(sys.argv[1]) != True:
    sys.exit("File does not exist")
# sprawdzamy czy plik ma rozszerzenie python ".py"
elif os.path.splitext(sys.argv[1])[1] != ".py":
    sys.exit("Not a Python file")

non_blank_count = 0
# Otwieramy plik i zliczamy linie, które nie są puste ani komentarzami
with open(sys.argv[1]) as infp:
    for line in infp:
        stripped_line = line.strip()

        # Ignorujemy puste linie oraz te zaczynające się od #
        if stripped_line and not stripped_line.startswith("#"):
            non_blank_count += 1

print(non_blank_count)
