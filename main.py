# Menu Items/data for Coffee Machine
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
# Resources in Coffee Machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Coin Values
quarter = .25
dime = .10
nickle = .05
penny = .01

# Coffee Machine State
on = True

# Function that reduces resources as they are used
def deduct_resources(water, coffee, milk):
    resources["water"] = resources.get("water") - water
    resources["coffee"] = resources.get("coffee") - coffee
    resources["milk"] = resources.get("milk") - milk

# Function that tracks the amount of money the customer entered
def customer_paid():
    num_quarters = float(input("How many quarters? ") or "0")
    num_dimes = float(input("How many dimes? ") or "0")
    num_nickles = float(input("How many nickles? ") or "0")
    num_pennies = float(input("How many pennies?") or "0")
    paid = quarter * num_quarters + dime * num_dimes + nickle * num_nickles + penny * num_pennies
    return paid

# Main program loop
while on == True:
    choice = input("What would you like? (espresso/latte/cappuccino: ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        print(resources)
    elif choice == "espresso":
        espresso = MENU.get("espresso", {}).get("ingredients")
        if resources.get("water") < espresso.get("water"):
            print("Sorry there is not enough resources.")
        elif resources.get("coffee") < espresso.get("coffee"):
            print("Sorry not enough coffee")
        else:
            paid = customer_paid()
            cost = MENU.get("espresso", {}).get("cost")
            if paid > cost:
                deduct_resources(espresso.get("water"), espresso.get("coffee"), 0)
                print("Here is your espresso. Enjoy!")
                print(f"Here is your change ${paid-cost}")
                resources["money"] = resources.get("money") + cost
            else:
                print(f"you have been refunded {paid}")
    elif choice == "latte":
        latte = MENU.get("latte", {}).get("ingredients")
        if resources.get("water") < latte.get("water"):
            print("Sorry there is not enough resources.")
        elif resources.get("coffee") < latte.get("coffee"):
            print("Sorry not enough coffee")
        elif resources.get("milk") < latte.get("milk"):
            print("Sorry there is not enough milk")
        else:
            paid = customer_paid()
            cost = MENU.get("latte", {}).get("cost")
            if paid > cost:
                deduct_resources(latte.get("water"), latte.get("coffee"), latte.get("milk"))
                print("Here is your latte. Enjoy!")
                print(f"Here is your change ${paid - cost}")
                resources["money"] = resources.get("money") + cost
            else:
                print(f"you have been refunded {paid}")
    elif choice == "cappuccino":
        cappuccino = MENU.get("cappuccino", {}).get("ingredients")
        if resources.get("water") < cappuccino.get("water"):
            print("Sorry there is not enough water.")
        elif resources.get("coffee") < cappuccino.get("coffee"):
            print("Sorry not enough coffee")
        elif resources.get("milk") < cappuccino.get("milk"):
            print("Sorry there is not enough milk")
        else:
            paid = customer_paid()
            cost = MENU.get("latte", {}).get("cost")
            if paid > cost:
                deduct_resources(cappuccino.get("water"), cappuccino.get("coffee"), cappuccino.get("milk"))
                print("Here is your cappuccino. Enjoy!")
                print(f"Here is your change ${paid - cost}")
                resources["money"] = resources.get("money") + cost
            else:
                print(f"you have been refunded {paid}")
