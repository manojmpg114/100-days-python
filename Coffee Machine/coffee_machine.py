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
    "money" : 0
}

#order = input("What would you like?: ") #Need to loop this for as long as the machine is running
#need a case were order = 'off' to exit the code all together, sys.exit
#when order = 'report' print the current resources report with accurate levels 

#if resources not enough for order, print "Sorry there is not enough water/milk/coffee"

#process coins should be it's own method 
#if there is enough resources for the order, the program should ask to enter how many of each coins
#[quarter, dime, nickel, penny]
#calculate the payment -- if not enough print "Sorry that's not enough money. Money refunded."

#if payment is enough, check if any change is due and then offer change: "Here is $2.45 dollars in change. <- round to 2 decimal points"
#change resource values to dispense the order

#after resources are modified and money accounted for, print "Here is your latte/expresso/cappucino. Enjoy!"
def run_report(order):
    """Run the report of resources, returns nothing"""
    if order == 'report':
        print(f"Water : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}\nMoney : ${resources['money']}")

def check_resources(order):
    """Check resources for a specific order, return True if we have enough to make the order"""
    water_status = True
    milk_status = True
    coffee_status = True

    for key in MENU:
        if order == key:
            for item in MENU[order]['ingredients']:
                #print(item)
                if resources[item] >= MENU[order]['ingredients'][item]:
                    continue
                else:
                    if item == 'water':
                        water_status = False
                    elif item == 'milk':
                        milk_status = False
                    elif item == 'coffee':
                        coffee_status = False
        
    if water_status == False:
        print('Sorry there is not enough water.')
        return False
    
    if milk_status == False:
        print('Sorry there is not enough milk.')
        return False
    
    if coffee_status == False:
        print('Sorry there is not enough coffee.')
        return False
    
    return True

def manage_order(order, money_dict):
    """Check if the money provided is enough to pay for the selected item, if so check if its more and offer change"""
    total_offered = 0
    cost = MENU[order]['cost']

    for coin in money_dict:
        if coin == 'quarter':
            total_offered += money_dict[coin]*0.25
        elif coin == 'dime':
            total_offered += money_dict[coin]*0.1
        elif coin == 'nickel':
            total_offered += money_dict[coin]*0.05
        elif coin == 'penny':
            total_offered += money_dict[coin]*0.01
    
    if total_offered > cost:
        print(f'Money Accepted, offering ${total_offered-cost} in change')
        return cost #change this to adding money to resources + subtracting resources to make the order
    elif total_offered == cost:
        print(f'Vending {order}')
        return cost #change this to adding money to resources + subtracting resources to make the order
    else:
        print('Not enough money, returning money')
        return 0 #can remove this return once we change how the method processes

def run():
    """Take the order and check if it is possible, if so collect the money and serve the order, runs the machine and reports"""
    order = input("What would you like?: ").lower()

    if order == 'off':
        return False #plug into a while loop to terminate
    if order == 'report':
        run_report(order)
    if check_resources(order):
        print('We have enough') #Time to put code / logic / methods relataed to accepting money and dishing out the order
        resources["money"] = manage_order(order,{'quarter' : 1, 'dime': 2, 'nickel': 3, 'penny': 4})
    


run()
