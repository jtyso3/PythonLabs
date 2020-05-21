
user_name = 'Andy'
print('Hello {}, it\'s nice to meet you!'.format (user_name))# Python 3.x
print(f'Hello {user_name}, it\'s nice to meet you!')# Python 3.4+ shortcut
print('Hello %s, it\'s nice to meet you!' % user_name)  # Python 2.x method
#Shortcuts insert variable user_name

city = 'Minneapolis'
temp = 67
chance_precip = 40
parking = 20.00
guests = 1000
print(f'Welcome!\n{city} Hilton Today')
print('{0:.<18}{1:.>5d}f'.format('Temperature', temp))
print('{:.<18}${:.>5.2f}'.format('Parking', parking))
print('{:.<18}{:.>5d}%'.format('Chance Precip', chance_precip))
print('{:.<18} {:.>5,d}'.format('Guests', guests))

'''
\n= next line, {0:.<18}{1:.>5d}f'.format('Temperature', temp)) 0= placeholder, : = unknown, 
. = optional fill character tab, 18 = unknown, 5 = column width, .2f = sets digits after decimal,
.format(parameters,of columns)
'''


name1 = input('Please type your name here >>> ')
print('Hello, ' + name1 + '!')

number_of_cds = int(input('How many CDs do you own?'))
age = float(input('Enter your age - use decimal for partial year.'))

print( "hello" + str(3))