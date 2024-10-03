import re

x = input("Podaj nazwe pliku: ")

y = re.sub(r"([A-Z])", r"_\1", x).lower()
print(y)
"""
Moduł re pozwala na dopasowywanie, wyszukiwanie, zamianę i manipulowanie 
ciągami znaków za pomocą wzorców wyrażeń regularnych.

Funkcja sub() z modułu re pozwala na zastąpienie części tekstu,
która pasuje do wzorca, nową wartością.

r'([A-Z])':

Ten wzorzec wyrażenia regularnego ([A-Z]) szuka wszystkich wielkich liter w ciągu znaków.
[A-Z] oznacza zakres wielkich liter (od A do Z).
Nawiasy () oznaczają grupę dopasowań — pozwala to później odwołać się do dopasowanych wielkich liter.

r'_\1':

To zastępuje dopasowane wielkie litery, dodając podkreślenie _ przed każdą wielką literą.
\1 odnosi się do pierwszej grupy dopasowań (czyli tej zawartej w nawiasach w wyrażeniu regularnym ([A-Z])), czyli konkretnej wielkiej litery.
Przykład: Jeśli w x znajduje się tekst MyFileName, to zostanie zamieniony na _My_File_Name (podkreślenia przed wielkimi literami).

"""
