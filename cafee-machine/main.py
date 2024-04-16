from data import MENU,resources


profit = 0
is_on = True

def is_ingedient_enaugh(order_ingerdients):
    for order_ingredient in order_ingerdients:
        if order_ingerdients[order_ingredient] >= resources[order_ingredient]:
            print(f"sorry there is not enaough {order_ingredient}")
            return False
    return True

def process_coin():
    print("Please insert coins")
    quaters = int(input("How many quaters?: ")) * 0.01
    nickles = int(input("How many nickles?: ")) * 0.05
    dimes = int(input("How many dimes?: ")) * 0.1
    pennies = int(input("How many pennies?: ")) * 0.25
    return  quaters + dimes + nickles + pennies

def is_transaction_succes(money_received,ingredient_cost):
    if money_received >= ingredient_cost:
        global profit
        profit =+ingredient_cost
        change = money_received - ingredient_cost
        print(f"here is your change {change}")
        return True
    print("you dont have enaught ressources")
    return False
def make_cafe(menu_choosed):
    for item in menu_choosed:
        resources[item] =-menu_choosed[item]

    


while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"water: {resources['water']},")
        print(f"milk: {resources['water']},")
        print(f"cofee: {resources['water']},")
        print(f"profit: {profit},")
    else:
        drink = MENU[choice]
        if is_ingedient_enaugh(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_succes(payment,drink["cost"]):
                make_cafe(drink["ingredients"])

        
      
   



  
      

  

""" 
1- y'a til des ressource dans la machine ? creer une fonction qui fait return True false pour dire ressource disponible
   a-  si oui 
        1-a creer une fonction qui comptabilise combien d'argent est mis dans le terminal,
        2- creer une fonction qui compabilise le choix du client
        3-creer une fonction qui compare le choix du café du client et l'argent mis par lui {elle dire combien rendre la monei, actualiser les ressources, et printer les resultat }
        4-creer une fonction pour printer les resulat
   
"""
   

