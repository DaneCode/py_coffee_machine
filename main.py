from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
menu = Menu()
menuItem = MenuItem
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while on == True:
    choice = input("What would you like? (espresso/latte/cappuccino: ").lower()
    if choice == "off":
         on = False
    if choice != "report":
        choosen_drink = menu.find_drink(choice)
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choosen_drink != None:
        if coffeeMaker.is_resource_sufficient(choosen_drink) == True:
            if moneyMachine.make_payment(choosen_drink.cost) == True:
                coffeeMaker.make_coffee(choosen_drink)
