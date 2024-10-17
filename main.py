from importlib.resources import open_text


def budget():
    print("Input the amount you want to deposit")
    money_dep = float(input("Enter amount: "))
    print(f"Money deposited: {money_dep}")

    food_total = 0
    car_total = 0
    rent_total = 0
    others_total = 0
    print("Select category you want to deposit in (using 1,2,3,4): ")
    print("Food")
    print("Car")
    print("Rent")
    print("Other")
    user_input = input("Enter: ")
    if user_input == "Food":
        food_total += money_dep
        print(food_total)
    if user_input == "Car":
        car_total += money_dep
        print(car_total)
    if user_input == "Rent":
        rent_total += money_dep
        print(rent_total)
    if user_input == "Other":
        others_total += money_dep
        print(others_total)
    stop=input('If you are finished enter "1" to exit: ')
    print('If you want to check all curent balance enter "2"')

budget()
