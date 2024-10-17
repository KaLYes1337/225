from importlib.resources import open_text


def budget():
    print("Input the amount you want to deposit")
    money_dep = float(input("Enter amount: "))
    print(f"Money deposited: {money_dep}")

    food_total = 0
    car_total = 0
    rent_total = 0
    others_total = 0
    print("Select category you want to deposit money into: ")
    print("Food")
    print("Car")
    print("Rent")
    print("Other")
    print('When you finish type "exit"')
    
    while True:
        user_input = input("Enter: ").upper()
        if user_input == "EXIT":
            break
        elif user_input =="FOOD":
            food_total+=money_dep  
            print(f"Total money spent for food: {food_total}")
        elif user_input=="CAR":
            car_total+=money_dep 
            print(f"Total money spent for car: {car_total}")
        elif user_input =="RENT":
            rent_total_total+=money_dep  
            print(f"Total money spent for rent: {rent_total}")
        elif user_input=="OTHER":
            others_total+=money_dep     
            print(f"Total money spent for other things: {others_total}")
    print("Have a nice day!")   
budget()
