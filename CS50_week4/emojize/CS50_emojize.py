emoticons = {  # dict/ slownik
    ":1st_place_medal:": "🥇",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    ":thumbsup:": "👍",
    ":earth_asia:": "🌏",
    ":candy:": "🍬",
    ":ice_cream:": "🍨",
}

x = input("Input: ")


def replace_emoticons(text):
    for (
        name,
        symbol,
    ) in emoticons.items():  # funkcja ktora bierze wartosc tekstowa i szuka pokolei
        text = text.replace(
            name, symbol
        )  # zamienia text na emotikone a nastepnie ja zwraca
    return text


wynik = replace_emoticons(x)

print("Output: " + wynik)
