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

from data import MENU,resources
inventaire = resources
def print_report(report):
         for key in report:
             print(f"{key}: {report[key]}")




def cost(inventaire,choice,MENU):

    print("Please insert coins")
    quaters = int(input("How many quaters?: ")) * 0.01
    nickles = int(input("How many nickles?: ")) * 0.05
    dimes = int(input("How many dimes?: ")) * 0.1
    pennies = int(input("How many pennies?: ")) * 0.25

    total = quaters + dimes + nickles + pennies
    if total >= MENU[choice]["cost"]:
        is_true = False
        for ingredient in MENU[choice]["ingredients"]:
            if inventaire[ingredient] > MENU[choice]["ingredients"][ingredient]:
                inventaire[ingredient] = inventaire[ingredient] -  MENU[choice]["ingredients"][ingredient]
                is_true = True
        if is_true:
            change = round(total - MENU[choice]["cost"])
            print(f"Here is {change} in change.\n Here is your latte ☕️. Enjoy!")
            return inventaire
        elif is_true == False:
            print("Sorry that's not enough ingedient")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return inventaire

is_on = True    

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):") 
    if choice == "off":
        is_on = False
    if choice == "report":
        print_report(inventaire)

    if choice == "latte" or choice == "espresso" or choice == "cappuccino":
        inventaire = cost(resources,choice,MENU)
        print_report(inventaire)
    

""" 
1- y'a til des ressource dans la machine ? creer une fonction qui fait return True false pour dire ressource disponible
   a-  si oui 
        1-a creer une fonction qui comptabilise combien d'argent est mis dans le terminal,
        2- creer une fonction qui compabilise le choix du client
        3-creer une fonction qui compare le choix du café du client et l'argent mis par lui {elle dire combien rendre la monei, actualiser les ressources, et printer les resultat }
        4-creer une fonction pour printer les resulat
   
"""
   


