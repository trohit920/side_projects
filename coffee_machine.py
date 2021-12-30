MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_continue = True
profit = 0

def resource_sufficient(choice):
    for items in MENU[choice]['ingredients']:
        if resources[items] > MENU[choice]['ingredients'][items]:
            return True
        else:
            print(f"Sorry there is not enough {MENU[choice]['ingredients'][items]}.")
            return False
    return True

def process_coin():
    global profit
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    price = quarter * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if price >= MENU[choice]['cost']:
        change = price - MENU[choice]['cost']
        print(f"Here is ${round(change, 2)} dollars in change.")
        profit += MENU[choice]['cost']
        print(profit)
        return True
    else :
        print("“Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print(f"Here is your {choice}. Enjoy!")

while is_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        is_sufficient = resource_sufficient(choice)
        if is_sufficient:
            is_money = process_coin()
            if is_money:
                make_coffee(MENU[choice]['ingredients'])

