'''
Jacob Tyson
10/17/2019
MidTermPractice 3
This program will take in user input about living expenses and then add them up for a grand total
'''


def main():                                                                             #Runs the program
    billcost, bills = inputs()
    total = processing(billcost)
    outputs(bills, billcost,total)
    restart = input('Would you like to continue? y or n.')
    if restart == 'y':
        print('OK, let\'s see a new score.')
        main()
    else:
        print('Thanks for using the program.')


def inputs():                                                                       #Gather User Input
   bills = ['Rent', 'Food', 'Transport', 'Other']                                   #List of Bills
   for cost in range(len(bills)):                                                   #Gathers input for cost of each bill puts it in list
        billcost = []
        for index in bills:
            print(f'How much do you need for {index}?')
            cost = input('Please enter to the nearest dollar amount?')
            while cost.isnumeric() is False:
                cost = input('please enter a whole number')

            billcost.append(cost)

        return billcost, bills

def processing(billcost):                                                               #Adds up a total of all bills
    total = 0
    for cost in billcost:
        total = total + int(cost)
    return total

def outputs(bills, billcost, total):                                                    #Formats output.
    print('Here\'s your overall budget:')
    print(*bills)
    print(*billcost)
    print(f'Here is your total {total}.')
main()                                                                                      #Calls function.

