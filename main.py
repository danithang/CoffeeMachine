# putting this at the top as the global variable because it needs to be called outside all functions
resource_money = 0
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


def coins():
    """Returns the total calculated from coins inserted"""
    quarter = int(input("Quarters: "))
    dime = int(input("Dimes: "))
    nickel = int(input("Nickels: "))
    penny = int(input("Pennies: "))

    # reassigning each coin variable to multiply the amount each is worth by how many coins user puts in
    quarter *= .25
    dime *= .10
    nickel *= .05
    penny *= .01

    # adding the coins up to get total they put in and returning the new variable coin_input
    coin_input = quarter + dime + nickel + penny
    return coin_input


def successful_transaction(money_received, coffee_cost):
    """Return True if payment is accepted and False if not enough coins"""
    if money_received <= coffee_cost:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    else:
        # rounded the difference 2 decimal places...subtracting money received from user from coffee cost
        change = round(money_received - coffee_cost, 2)
        print(f"Here is your ${change} in change")
        # resource_money won't work in local variable so global variable needs to be called for it to work
        global resource_money
        # if money inserted is greater or equal to coffee_cost then we add to resource_money variable which is adding
        # to the machine
        resource_money += coffee_cost
        return True


# defining sufficient resources and inputting ingredients for each choice
# also proving that is_enough is True until the ingredients are greater than the resources then will return False
# also returning is_enough
def sufficient_resources(order_ingredients):
    """Returns True when order can be made, False when there are not enough resources"""
    is_enough = True
    # using for loop to get each item in the dictionary of ingredients
    for item in order_ingredients:
        # comparing each item in order ingredients to each item in resources
        # to see if there is enough resources for each drink
        if order_ingredients[item] >= resources[item]:
            # adding item from for loop to tell user which item they don't have enough of
            print(f"Sorry, you do not have enough {item}.")
            is_enough = False
        return is_enough


# input a statement to ask what user wants (coffee_name) and deduct from resources
# for loop to make sure the prompt repeats after every transaction
def make_coffee(coffee_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name} ☕. Enjoy!")


# starting while loop to repeat the program
start_transaction = True
while start_transaction:
    coffee_choice = input("Would you like an: 'espresso', 'latte', or 'cappuccino'? Type 'report' to get resources or "
                          "'off' to turn off the machine. ")
    # check user input for which choice they make, ask for resources, or turn off machine if user wants
    if coffee_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resource_money}")
    elif coffee_choice == 'off':
        start_transaction = False
    # putting the dictionary menu and coffee choice in a variable then adding a function and outputting the
    # ingredient dictionary to cover each possible choice
    else:
        coffee = MENU[coffee_choice]
        if sufficient_resources(coffee['ingredients']):
            print("Insert Money")
            # calling function and outputting the function coins()...putting it in a variable of payment
            # to output that in the successful_transaction function
            payment = coins()
            # calling function and outputting payment and variable coffee and pulling cost of each coffee
            if successful_transaction(payment, coffee['cost']):
                make_coffee(coffee_choice, coffee['ingredients'])


