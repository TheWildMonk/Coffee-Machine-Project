# Import necessary libraries
from data import MENU, resources


# Function for check whether the coffee machine has enough resource.
def is_resource_sufficient(coffee_ingredients):
    """The function takes the amount of ingredients needed for user's coffee and return
    a boolean value.
    Not enough resource --> False
    Enough resource --> True"""
    for key in coffee_ingredients:
        if coffee_ingredients[key] > resources[key]:
            print(f"There is not enough {key}.")
            return False
    return True


# Function to process the user provided coins in the machine.
def process_coins(coffee, quarter, dime, nickle, penny):
    """The function takes user's coffee choice along with provided coins for the coffee.
    If there is not enough coins, the money is refunded. Otherwise, it gives the change to the
    user and serves the coffee."""
    global money
    coin_value = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    if coin_value < MENU[coffee]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(coin_value - MENU[coffee]['cost'], 2)} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        money += MENU[coffee]['cost']
        deduct_resources(coffee)


# Function to deduct coffee resources after a successful transaction in the coffee machine.
def deduct_resources(coffee):
    """The function takes user's coffee choice and deduct the ingredient of the coffee from
    the machine resources."""
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] = resources[ingredient] - MENU[coffee]["ingredients"][ingredient]


# List of coffee choices present in the coffee machine.
coffee_choices = ["espresso", "latte", "cappuccino"]

# Main coffee machine functionality.
money = 0.0
machine_start = True
while machine_start:
    # Ask user for either current status of the machine, a coffee choice or t
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_choice in coffee_choices:
        ingredients = MENU[user_choice]["ingredients"]
        coffee_cost = MENU[user_choice]["cost"]
        if is_resource_sufficient(ingredients):
            print("Please insert coins.")
            quarters = float(input("How many quarters?: $"))
            dimes = float(input("How many dimes?: $"))
            nickles = float(input("How many nickles?: $"))
            pennies = float(input("How many pennies?: $"))
            process_coins(user_choice, quarters, dimes, nickles, pennies)
    elif user_choice == "off":
        machine_start = False
    else:
        print("Wrong choice, please try again!")
