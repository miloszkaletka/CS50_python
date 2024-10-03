import datetime  # służy do pracy z datami i godzinami.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:

        userdate = input("Date: ").strip()

        date_formats = ["%B %d, %Y", "%m/%d/%Y", "%d.%m.%Y"]  # lista akceptowalnych dat

        for date_format in date_formats:
            try:
                date_obj = datetime.datetime.strptime(
                    userdate, date_format
                )  # próbuje przekształcić wprowadzone dane w obiekt daty.
                formatted_date = date_obj.strftime(
                    "%Y-%m-%d"
                )  # jezeli format daty pasuje to program przeksztalca ja
                print(formatted_date)

                # Program pobiera numer miesiaca (np. 1 dla stycznia).
                month_index = date_obj.month
                month_name = months[
                    month_index - 1
                ]  # -1 poniewaz lista zaczyna sie od 0
                return  # zwracamy nazwe miesiaca
            except ValueError:
                pass

        else:
            print("Invalid date format. Please try again.")


main()
