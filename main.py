# Import necessary libraries
from data import MENU, resources

# Creating variables
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

close_machine = False
while not close_machine:

    # TODO: 1. Ask the user for their choice of either coffee or the report of current status of the coffee machine
    #  or stop the machine.
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. If user asks for the report, provide the current status of the report.
    #  Else ask user for coins.
    if user_choice == "off":
        close_machine = True
    elif user_choice == "report":
        print(f"Water: {water}ml\n"
              f"Milk: {milk}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${money}")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":

        # TODO: 2a. If there's not enough resource, let user know and ask the user again.
        #  Else, ask the user for coins.
        if water < MENU[user_choice]["ingredients"]["water"] and milk < MENU[user_choice]["ingredients"]["milk"] and \
                coffee < MENU[user_choice]["ingredients"]["coffee"]:
            print(f"Sorry. there is not enough water 💧 for {user_choice}.")
        else:
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            user_money = quarters + dimes + nickels + pennies
            change = user_money - MENU[user_choice]["cost"]

            # TODO: 2b. If user didn't provided enough money, let the user know and refund the money.
            #  Else, give the change to user and serve the Coffee.
            if user_money < MENU[user_choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
                money = money
            else:
                if change != 0:
                    print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {user_choice} ☕, enjoy")

                # TODO: 2c. Deduct the resources used from original resources.
                if user_choice != "espresso":
                    water -= MENU[user_choice]["ingredients"]["water"]
                    milk -= MENU[user_choice]["ingredients"]["milk"]
                    coffee -= MENU[user_choice]["ingredients"]["coffee"]
                    money += MENU[user_choice]["cost"]
                else:
                    water -= MENU[user_choice]["ingredients"]["water"]
                    coffee -= MENU[user_choice]["ingredients"]["coffee"]
                    money += MENU[user_choice]["cost"]
    else:
        print("Please enter correct coffee name.")
