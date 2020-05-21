'''
Jacob Tyson
credit card validator
This program will ask user to input creditcard number, and validates it using different formats.
12/12/2019
'''
import re


def main():
    getCardNumber = inputs()  #  calls inputs
    getCardNumber = processing(getCardNumber)  # calls proccessing
    outputs(getCardNumber)  # calls outputs
    restart = input('Would you like to restart? y or n')  # restart feature
    restart = restart.lower()
    if restart == 'y':  # restart feature
        main()
    else:
        print('Thanks for using the program.')

def inputs():
    getCardNumber = input('Please enter your credit card number')  # get user input

    return getCardNumber

def processing(getCardNumber):
    compiler = re.compile(r'(\d\d\d\d+)([.]|[-]|\s )+(\d\d\d\d+)([.]|[-]|\s )+(\d\d\d\d+)([.]|[-]|[,] )+(\d\d\d\d+)')  # regex card number validator

    while compiler.search(getCardNumber) == None:  # validator
        getCardNumber = input('I am sorry our records do not recognize that number.\n Please use the followong format:\n xxxx.xxxx.xxxx.xxxx or xxxx-xxxx-xxxx-xxxx or xxxx,xxxx,xxxx,xxxx')


    return getCardNumber  # returns validated card number.


def outputs(getCardNumber):
    print(f' Success!!!! \n Your card number is: {getCardNumber}!!')  # displays output

main()