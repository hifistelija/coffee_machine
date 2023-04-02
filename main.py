from info import MENU, resources


def print_resources():
    for resource, amount in resources.items():
        print(f"{resource}: {amount}")


def make_drink(drink_name, money):
    """Proses drink and money"""
    cost = MENU[drink_name]["cost"]
    if money < cost:  # check if money given is less than cost of drink selected
        print(f"Sorry, {cost - money:.2f} dollars more needed.")
        return False
    for ingredient, amount in MENU[drink_name]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    for ingredient, amount in MENU[drink_name]["ingredients"].items():  # deduct resources from inventory
        resources[ingredient] -= amount
    change = money - cost
    if change > 0:  # proses change
        print(f"Here is {change:.2f} dollars in change.")
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    total = quarters * monetary_value["quarter"] + dimes * monetary_value["dime"] + \
            nickels * monetary_value["nickel"] + pennies * monetary_value["penny"]
    return total


user_options = {
    "report": print_resources,
    "latte": lambda: make_drink("latte"),
    "espresso": lambda: make_drink("espresso"),
    "cappuccino": lambda: make_drink("cappuccino")
}

monetary_value = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}


def menu():
    selection = ""
    while selection != "off":
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection in user_options:
            selected_function = user_options[selection]
            if selection != "report":
                money = process_coins()
                if money:
                    success = make_drink(selection, money)
                    if not success:
                        print("Transaction failed. Please try again.")
            else:
                selected_function()
        elif selection == "off":
            print("Shutting down machine..")
        else:
            print("Unknown command. Please ty again")


menu()
