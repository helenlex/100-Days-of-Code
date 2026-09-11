"""Trying to rewrite coffee machine script with objects"""

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

on = True

coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()


while on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        on = False
    elif order == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        order = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(order) is True:
            make_payment = moneymachine.make_payment(order.cost)
            if make_payment is True:
                coffeemaker.make_coffee(order)
