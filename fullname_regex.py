'''
Jacob Tyson
Title: Full Name validator
Description: This program will take in user input of their name, and validate to make sure the user put in the correct characters
for a name and then will print the name.
'''
from validator_collection import validators
from giturlparse import parse  # obtain module from github
import re # Imports regex

while True: #Validation purposes
    name_source = input('Please Enter your full name: First Middle Last') #gets user input
    namePattern = re.compile(r'(^([a-zA-Z]+[\']*[-]* *)+$)') #creates pattern that must be followed
    check = namePattern.search(name_source) #check user input follows pattern
    if check == None: #validates
        print('That is not a name') #Lets user know to try again/ starts program from top of while loop
    else:
        print('Here is the name: ' + check.group()) #prints name
        break #breaks out of loop