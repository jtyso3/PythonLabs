#Jacob Tyson area-calculator
print(f'Welcome to the rectangle calculator!')
#Variables
unit = input('What is your unit of measurement?(in, ft, cm)')
width = input('What is the rectangles width?')
height = input('What is the rectangles height?')
#formula
area = (float(width) * float(height))
#Output
print('{:<1}{:<1}{:<1}{:<1}'.format('your area of the rectangle is ', round(area, 2), 'sq',str(unit)))

