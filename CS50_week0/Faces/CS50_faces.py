def convert(smutna):
    smutna = smutna.replace(":(", "🙁")
    smutna = smutna.replace(":)", "🙂")
    return smutna


x = input("give me text with smile or sad face: ")
wynik = convert(x)
print(wynik)
