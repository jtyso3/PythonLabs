'''
Jacob Tyson
10/16/2019
Title: Pastry shop invoice calc
This program will calculate the total cost of buying Cornish Pastries, and creates an invoice with the price, tax,
tip and final total
'''

def main():
    pastryAmount, deluxe, average, tipAmount = inputs()




def inputs():
    pastryAmount = input('how many pastries would you like today?')
    if pastryAmount.isnumeric() is False:
        pastryPrice = input('Please enter a whole number.')
    while True:
        print('How many of each kind of pastry would you like today?')
        deluxe = input('How many deluxe pastries?')
        if deluxe.isnumeric() is False:
            deluxe = input('Please enter a whole number')
        average = input('How many regular pastires would you like today?')
        if average.isnumeric() is False:
            average = input('Please enter a whole number.')
        if average + deluxe != pastryAmount:
            print('That does not add up, Would you like new total? y or n')
            if 'y':
                pastryAmount = average = deluxe
            else:
                if 'n':
                    main()
        break


    tipAmount = input('How much of a tip % would you like to leave?')
    if tipAmount.isnumeric() is False:
        tipAmount = input('Please enter a whole number.')



    return pastryAmount, deluxe, average, tipAmount

def processing():
    stateTax = .07025
    deluxePastry = 5
    averagePastry = 3











minntax = .07025 #Static value of  tax
pastryPrice = input('Please Enter the price of your pastries?') #User input of amount pastry's cost
pastryPrice = float(pastryPrice)  #converts pastry to float value

Tip1 = input('Please enter the tip percentage you want to give') #User input for percentage of tip
Tip2 = int(Tip1) / 100 #calculates total amount of tip, makes tip1 a integer

totalTip = Tip2 * pastryPrice #calculates the tip
total_with_tip = (Tip2 * pastryPrice) + pastryPrice #calculates total cost with tip

tax = round(pastryPrice * minntax, 2) #calculate the tax and rounds 2 decimal places.
subtotal = float(pastryPrice) + tax #Calculates subtotal
Grandtotal = round(total_with_tip + tax, 2) #Calculatesgrand total and round to 2 decimal places
#formats Outputs.
print('Invoice Due')
print('{:<20}{:>3}{:>8,.2f}'.format('Pastry Price', '$', pastryPrice))
print('{:<20}{:>3}{:>8,.2f}'.format('Tax @ 7.025%', '$', tax))
print('{:<20}{:>3}{:>8,.2f}'.format('Subtotal', '$', round(subtotal, 2)))
print('{:<20}{:>3}{:>8,.2f}'.format(f'Tip @ {Tip1}%', '$', round(totalTip, 2)))
print('{:<20}{:>3}{:>8,.2f}'.format('Total', '$', Grandtotal))
