def convert(time):
    g, m = map(int,time.split(":"))
    return g + m /60

def main():
    x = input("What time is it? ")
    wynik = convert(x)
    
    if 7.0 <= wynik <= 8.0:
        print("breakfast time")
    elif 12.0 <= wynik <= 13.0:
        print("lunch time")
    elif 18.0 <= wynik <= 19.0:
        print("dinner time")
    else:
        print("Not meal time") 


if __name__ == "__main__":
    main()
