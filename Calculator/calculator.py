#calculator.py
from art import logo
import os

def add(n1,n2): #Add
    return n1+n2

def subtract(n1,n2): #Subtract
    return n1-n2

def divide(n1,n2): #Divide
    if n2 == 0:
        return
    else:
        return n1/n2
    
def multiply(n1,n2): #Multiply
    return n1*n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    
    for op in operations:
        print(op)
        
    op_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("Whats the second number?: "))

    answer = operations[op_symbol](num1,num2) #extra step could be; calc_function = operations[op_symbol]

    # calc_func = operations[op_symbol]
    # answer = calc_func(num1,num2)

    print(f"{num1} {op_symbol} {num2} = {answer}")
    
    more_calc = False

    if 'y' == input(f"Type 'y' to continue calculating with {answer}: ").lower():
        more_calc = True

    
    while more_calc:
        next_num = float(input("What's the next number?: "))
        for op in operations:
            print(op)
        
        op_symbol = input("Pick an operation from the line above: ")
        prev_answer = answer
        answer = operations[op_symbol](prev_answer,next_num)
        
        print(f"{prev_answer} {op_symbol} {next_num} = {answer}")
        
        if 'y' == input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower():
            more_calc = True
        else:
            more_calc = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()

calculator()