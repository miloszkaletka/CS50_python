import string


def main():
    value()


def value(greeting):
    x = input("Greeting: ").strip()
    slowo = x.split()[0].strip(string.punctuation)

    if slowo.lower() == "hello":
        return 0
    elif slowo.lower()[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
