from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


while True:
    option = input(f"What would you like? {menu.get_items()}: ")
    if option == "off":
        break
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option not in menu.get_items().split('/'):
        menu.find_drink(option)
    else:
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





#menu.find_drink(input(f"What would you like? {menu.get_items()}: "))

