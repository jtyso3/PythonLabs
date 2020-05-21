'''
Jacob Tyson
Chapter 5 ppt exercise file
'''
#slide 4
print('slide 4')
print('Dictionary data type: stores key- value pairs.')
scores = {'Al':5, 'Betty':9, 'Cole':8, 'Bea':1}
print(scores)


#slide 5
print('slide 5')
print('adding a new score')
scores['Dora'] = 7

print('modifying a score')
scores['Al'] = 6
print(scores)

#slide 7
print('slide 7')
# Remodeling? Use a list of rooms that you need to paint.
rooms = ['Kitchen', 'Bedroom', 'Bathroom']
# if you painted the bedroom…
rooms.remove('Bedroom')
# if you need to add the hallway…
rooms.append('Hallway')
print(rooms)

#slide 8
print('slide 8')
# By contrast, use a dictionary to store the paint color for every room.
roomsNcolors = {'Kitchen':'Blue', 'Bedroom':'Green', 'Bathroom':'Pink'}
# when you have painted the bedroom
roomsNcolors.pop('Bedroom')
# Need to paint the hallway?
roomsNcolors['Hallway'] = 'Beige'
# What color was the kitchen supposed to be? – here's how to retrieve:
kitchen_color = roomsNcolors['Kitchen']
print('The kitchen will be painted ' + kitchen_color)

#slide 9
print('slide 9')
# you can have strings as both keys and values
countries = {'CA': 'Canada', 'US': 'United States',  'MX': 'Mexico', 'GB': 'Great Britain'}

# you can have numbers as keys, strings as values
numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# you can have strings as keys, mixed types as values
book = {'name': 'Automate the Boring Stuff',  'year': 2018, 'price': 18.99 }

# how to initialize a variable as an empty dictionary
book_catalog = {}

# This code pulls out a value from the countries dictionary, but has risks
country = countries['MX']   # "Mexico"
#country = countries['IE']   # KeyError: Key doesn't exist

#Here is one way to prevent the error, for your excercise file
#slide 10
print('slide 10')
code = 'IE'   # or replace with user-defined search term
if code in countries:
    country = countries[code]
    print(country)
else:
	print('There is no country for code: ' + code)

#slide 12
print('slide 12')
#bothgive the same ouptput
for code in countries:
    print(code + '\t' + countries[code]) #This is a nice formatting tool, so it seems.

for code in countries.keys():   #Uses the keys in dictionary
    print(code + '\t' + countries[code])

#slide 13
print('slide 13')
for code, country in countries.items(): #using the .items() will give both keys, and values
	print(code + '\t' + country)


#slide 14
print('slide 14')
#using the .values() method
for country in countries.values():   #uses values in dictionary
	print(country)

#slide 15
print('slide 15')
#using the .get() method.
country = countries.get('MX', 'No such country')	# "Mexico" prints, since the entry exists, "no such country' is default value
print(country)
country2 = countries.get('IE', 'No such country')	# "No such country" prints - shorter than conditional
print(country2)

#slide 16
print('slide 16')
#Syntax for deleting an item
del countries['MX'] #deleting item 'MX' from countries dictionary
#del countries['IE']		# KeyError: Key doesn't exist, check for value before deleting

check_code = 'IE'		# or replace with user search term
if check_code in countries:
	country = countries[check_code]
	del countries[check_code]
	print (country + ' was deleted.')
else:
	print ('There is no country for this code: ' + check_code )
#slide 17
print('slide 17')
# Code using the pop() method – deleted value is returned
country = countries.pop('US', 'Unknown')		# "United States" – deleted & returned, since entry exists
country2 = countries.pop('IE', 'Unknown')  	# "Unknown" – prevents error when no such code exists
print(f'Existing country deleted: {country} \tMissing country: {country2}')
print(countries)

# Code using the clear() method – can't be undone!
countries.clear()  # all deleted!
print(countries)
