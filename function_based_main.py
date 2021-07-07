# Import necessary libraries
from data import MENU, resources


# TODO: 2a(i). Create a function to check the resources.
def check_resources(choice):
    for item in resources:
        if MENU[user_choice]["ingredients"][item] > resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


# TODO: 2a(ii). Create a function to calculate the coin equivalent money user provided.
def calculate_coin():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


# TODO: 4a. Create a function to deduct the resources.
def update_resources(choice):
    for item in resources:
        resources[item] -= MENU[choice]["ingredients"][item]
    return resources


# TODO: 1. Ask the user for their choice of either coffee or the report of current status of the coffee machine
#  or stop the machine.
money = 0
close_machine = False
while not close_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice != "off" and user_choice != "report" and user_choice not in MENU:
        print("Please enter correct coffee name.")

    elif user_choice == "off":
        close_machine = True

    # TODO: 2. If user asks for the report, provide the current status of the report.
    #  Else ask user for coins.
    elif user_choice == "report":
        print(f"Water: {resources['water']}\n"
              f"milk: {resources['milk']}\n"
              f"coffee: {resources['coffee']}\n"
              f"Money: ${float(money)}")
    # TODO: 3. If there's not enough resource, let user know and ask the user again.
    #  Else, ask the user for coins.
    else:
        enough_resource = check_resources(user_choice)
        if enough_resource:
            total_coin_inserted = round(calculate_coin(),2)

            # TODO: 3a. If user didn't provided enough money, let the user know and refund the money.
            #  Else, give the change to user and serve the Coffee.
            if total_coin_inserted < MENU[user_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total_coin_inserted - MENU[user_choice]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here's your {user_choice} ☕. Enjoy!")

                # TODO: 4. Deduct the resources used from original resources and add money to the machine.
                update_resources(user_choice)
                money += MENU[user_choice]["cost"]
