import locale

locale.setlocale( locale.LC_ALL, '' )

num1 = int(input('Enter starting value: '))
goal = int(input('Enter target goal: '))

original = num1

years = 0
if num1 < goal:
    while num1<goal:
        #print(num1)
        num1 *= 1.07 #7% yearly return
        years +=1
    print(f'It would take {years} years to hit your goal of {locale.currency(goal, grouping=True )} if you invested {locale.currency(original, grouping=True )} and nothing more into the markets.\n')


print('For Personal Compounding, $30,000 per year calculations.\n')
years = 0
num1 = 30000
if num1 < goal:
    for year in range(int(input('How many years do you plan to invest? '))): #30 years
        num1 *= 1.07 #7%
        if years > 0:
            num1 += 30000
        years +=1
    
    total = locale.currency(num1, grouping=True )
    print(f'With consistent investments of $30,000 a year, in {years} years you would have {total}\n')
    
salary_contribution = int(input('Enter salary to invest: '))
investment_total = salary_contribution

years = 0

for year in range(int(input('How many years do you plan to invest? '))): #30 years
    investment_total *= 1.07 #7%
    if years > 0:
        investment_total += salary_contribution
    years +=1    
    
total = locale.currency(investment_total, grouping=True )

print(f'With consistent investments of {locale.currency(salary_contribution, grouping=True )} a year, in {years} years you would have {total}')