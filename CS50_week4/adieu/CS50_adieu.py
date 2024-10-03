import inflect

p = inflect.engine()  # biblioteka zawierajaca narzedzia
# do generowania sformulowan gramatycznych w ang

names = []

try:
    while True:  # nieskonczona petla
        n = input("Name: ")
        names.append(n)

# jezeli uzytkownika wywola EOF to program przechodzi do expect EOFerror
except EOFError:
    if names:
        namesko = p.join((names))
        # drukuje tekst w formacie: Adieu Adieu to: imie, imie and imie
        print("\nAdieu, Adieu to " + namesko)
