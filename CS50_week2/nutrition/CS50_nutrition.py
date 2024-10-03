fruits = {
    "Sweet Cherries": "Calories: 100",
    "Apple": "Calories: 130",
    "Avocado": "Calories: 50",
    "Banana": "Calories: 110",
    "Cantaloupe": "Calories: 50",
    "Grapefruit": "Calories: 60",
    "Grapes": "Calories: 90",
    "Honeydew Melon": "Calories: 50",
    "Kiwifruit": "Calories: 90",
    "Lemon": "Calories: 90",
    "Lime": "Calories: 20",
    "Nectarine": "Calories: 60",
    "Orange": "Calories: 80",
    "Peach": "Calories: 60",
    "Pear": "Calories: 100",
    "Pineapple": "Calories: 50",
    "Plums": "Calories: 70",
    "Tangerine": "Calories: 50",
    "Watermelon": "Calories: 50",
}


def main():

    fruit_name = input("Podaj owoc: ").title()  # zmienia pierwsze litery zdania na duze

    if fruit_name in fruits:
        print(f"{fruits[fruit_name]}")


main()
