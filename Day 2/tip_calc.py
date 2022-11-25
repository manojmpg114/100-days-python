#tip_calc.py

bill = float(input('Please enter the total bill: \n$'))
tip = float(input('What % tip do you want to provide? \n'))
people = int(input('How many people are splitting the bill? \n'))


total_due = bill*(1+(tip/100))
per_person = total_due/people

print(f'Each person should pay: ${per_person:.2f} to settle the bill.')

