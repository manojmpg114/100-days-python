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
        print(f'Money Accepted, offering ${total_offered-cost:.2f} in change') #if this was more legitimate round based on currency and account for full values to the penny
        
        resources["money"] += cost
        
        for resource in MENU[order]["ingredients"]:
            resources[resource] -= MENU[order]["ingredients"][resource]
            
        print(f'Vending {order}')
        return resources["money"]
    elif total_offered == cost:
        print(f'Vending {order}')
        resources["money"] += cost
        return resources["money"] 
    else:
        print('Not enough money, returning money')
        return resources["money"]

def run():
    """Take the order and check if it is possible, if so collect the money and serve the order, runs the machine and reports"""
    order = input("What would you like?: ").lower()

    if order == 'off':
        return False #plug into a while loop to terminate
    if order == 'report':
        run_report(order)
        
    if order != 'off' and order != 'report':
        if check_resources(order):
            
            print('We have enough')
            resources["money"] = manage_order(order,{
                'quarter' : int(input('Enter number of quarters: ')),
                'dime': int(input('Enter number of dimes: ')),
                'nickel': int(input('Enter number of nickles: ')),
                'penny': int(input('Enter number of pennies: ')),
                }) #change money input to user's choice later
    
    

#Running here didn't want to make a main

while True:
    if run() == False:
        break
