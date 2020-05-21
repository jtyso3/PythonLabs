#Jacob Tyson-Coffee shop profits
#coffee
coffeeCups = int(input('How many cups of coffee sold? '))
coffeePrice = float(input('Price of coffee? '))
coffee_sales = coffeeCups * coffeePrice
#tea
teaCups = int(input('How many cups of tea sold? '))
teaPrice = float(input('Price of tea? '))
tea_sales = teaCups * teaPrice
#cappuccino
cappCups = int(input('How many cups of cappucino sold? '))
cappPrice = float(input('Price of cappuccino? '))
capp_sales = cappCups * cappPrice
#total profit and cups
totalCups = coffeeCups + teaCups + cappCups
totalProfit = capp_sales + tea_sales + coffee_sales
#format
print(f'Total Sales for the reporting period')
print('{:<20}{:^20}{:>8}'.format('Type', 'Total cups', 'Total Sales'))
print('{:<20}{:^20}{:>8}'.format('Tea', teaCups, round(tea_sales, 2)))
print('{:<20}{:^20}{:>8}'.format('Coffee', coffeeCups, round(coffee_sales, 2)))
print('{:<20}{:^20}{:>8}'.format('Cappuccino', cappCups, round(capp_sales, 2)))
print('{:<20}{:^20}{:>8}'.format('Total', totalCups, round(totalProfit, 2)))
