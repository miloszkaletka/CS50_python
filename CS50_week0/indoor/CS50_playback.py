fast = input("Tell me something fast: ")
slow = "...".join(
    fast.split()
)  # split() dzieli teskt na wyrazy ["I", "am", "learning", "Python"]
print(slow)  # "..." oznacza ze funkcja join uzyje do polaczenia wyrazow 3 kropek
