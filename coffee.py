MENU = {
    "espresso": {
        "ingrediants":{
            "water":50,
            "coffee":18,
            "milk":10,
        },
        "cost": 150,
    },
    "latte":{
        "ingrediants":{
            "water":200,
            "coffee":150,
            "milk":150,
        },
        "cost":250,
    },
    "cappuccino":{
        "ingrediants":{
            "water":250,
            "milk":150,
            "coffee":24,
        },
        "cost":300,
    }
}

resources = {
    "water":3000,
    "coffee":2000,
    "milk":1000,
}
#************Report************
def print_report():
    print(f"Amount of Water left is {resources["water"]}ml")
    print(f"Amount of Coffee left is {resources["coffee"]}g")
    print(f"Amount of Milk left is {resources["milk"]}ml")

#************Check ************
#def check_order(order):
#    if order in MENU:
#        return True
#    else:
#        print(f"\nSorry, {order} is not a valid option.\n")
#        return False
        
#************Transactions************
def transactions():
    print("Enter Cash (500,100,50 only)")
    total_500 = int(input("500rs Notes:"))*500
    total_100 = int(input("100rs Notes:"))*100
    total_50 = int(input("50rs Notes:"))*50
    total = total_100 + total_50 + total_500
    return total

#************Check_money************
def check_money(paid,price):
    change = paid - price
    
    if change > 0:
        print(f"\nYour change is {change}rs.\n\nTake it from reciving counter.\n")
        return True
    elif change == 0:
        return True
    else:
        return False

#************Requirements************
def requirements(Order):
    milk_machine = resources["milk"]
    coffee_machine = resources["coffee"]
    water_machine = resources["water"]
    
    milk_order = MENU[Order]["ingrediants"]["milk"]
    coffee_order = MENU[Order]["ingrediants"]["coffee"]
    water_order = MENU[Order]["ingrediants"]["water"]
    if milk_machine >= milk_order and coffee_machine >= coffee_order and water_machine >= water_order:
        return True
    else:
        return False
  
  
#************Deduction************
def deduct(Order):
    milk_order = MENU[Order]["ingrediants"]["milk"]
    coffee_order = MENU[Order]["ingrediants"]["coffee"]
    water_order = MENU[Order]["ingrediants"]["water"]
    
    milk_machine = resources["milk"]
    coffee_machine = resources["coffee"]
    water_machine = resources["water"]
    
    resources["milk"] = milk_machine - milk_order
    resources["coffee"] = coffee_machine - coffee_order
    resources["water"] = water_machine - water_order
#************START************
print('''
    //   ) )           //  ) ) //  ) )                            
   //         ___   __//__  __//__  ___      ___                  
  //        //   ) ) //      //   //___) ) //___) )               
 //        //   / / //      //   //       //                      
((____/ / ((___/ / //      //   ((____   ((____                   
                                                                  
    /|    //| |                                                   
   //|   // | |     ___      ___     / __     ( )   __      ___   
  // |  //  | |   //   ) ) //   ) ) //   ) ) / / //   ) ) //___) )
 //  | //   | |  //   / / //       //   / / / / //   / / //       
//   |//    | | ((___( ( ((____   //   / / / / //   / / ((____    
    ''')

is_on = True

while is_on:
    printing = input("\nYou want to see report. (Yes/No)\n").lower()
    
    if printing == 'yes':
        print_report()
    elif printing == 'no':
        pass
    else:
        print("ERROR!")
        break
    order = input("\nWhat would you like? (espresso/latte/cappuccino)\n").lower()
    
    if order not in MENU:
        print(f"\nSorry, {order} is not a valid option.\n")
        break
    
    print(f"\nIt would be {MENU[order]["cost"]} for {order.capitalize()}\n")
    
    required = requirements(order)
    if required:
        #take money
        money = transactions()
        cost = MENU[order]["cost"]
        paid = check_money(money,cost)
        
        if paid:
            print(f"\nPlease collect your ☕ {order}!\n")
            
            deduction = deduct(order)
            
        else:
            print("\nThe amount paid is low please take your return.\n")
            break
        
        
        redo = input("You want to re-order something?\n(Yes/No)\n").lower()
        if redo == 'yes':
            is_on = True
        elif redo == 'no':
            print("Turning the machine off!")
            break
        else:
            print("ERROR!")
            break
        
    else:
        print("ERROR!")
        break
