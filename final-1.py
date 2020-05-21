'''
Jacob Tyson
10/24/19
Title: Cost of tour in Bejing China
Description: This program calculate the total cost of a trip to bejing china.
'''
import re
def main():
    numPeople, beachTrip, tourGuideGifts = inputs()  # calls inputs
    grandTotal, subTotal, activityFees, totHotelCost, sideTripCost, totGift = processing(numPeople, beachTrip, tourGuideGifts)  # calls proccessing
    output(totHotelCost, activityFees, sideTripCost, totGift, subTotal,grandTotal, numPeople, beachTrip,tourGuideGifts)  # calls outputs
    restart = input('Would you like to restart? y or n')
    restart = restart.lower()
    if restart == 'y':  #  restart feature
        main()
    else:
        print('Thanks for using the program.')





def inputs():

    numPeople = input('How many people are in your party?')  # get num people/ validate whole number
    while numPeople.isnumeric() is False:
        numPeople = input('please enter a whole number')
    numPeople = int(numPeople)

    beachTrip = input('how many people will go on the optional beach trip?')  # get beach trip validate whole number
    while beachTrip.isnumeric() is False:
        beachTrip = ('Please enter a whole number')
    beachTrip = int(beachTrip)


    tourGuideGifts = input('What percentage will you give toward host gifts (3-5%)')  # get gift amount validate float number
    compiler = re.compile(r'[.]+')
    while compiler.search(tourGuideGifts) == None:
        tourGuideGifts = input('please enter a floating number')
    tourGuideGifts = float(tourGuideGifts)

    return numPeople,beachTrip, tourGuideGifts

def processing(numPeople, beachTrip, tourGuideGifts): #  makes total caluclations
#Calculating total cost
    hotel = 375
    activity = 150
    tainjin = 100

    totHotelCost = numPeople * hotel #Total hotel cost  # calc total hotel costs
    totHotelCost = round(totHotelCost, 2)

    activityFees = activity * numPeople #Total activity cost  # calcs total activity costs
    activityFees = round(activityFees, 2)

    sideTripCost = beachTrip * numPeople #calc total side trip cost
    sideTripCost = round(sideTripCost, 2)


    subTotal = totHotelCost + activity + sideTripCost #calc total side trip cost
    subTotal = round(subTotal, 2)         #round 2 decimal

    totGift = (tourGuideGifts / 100) * subTotal     #calc total amount of gift
    totGift = round(totGift, 2)

    grandTotal = subTotal + totGift    #calculate grand total
    grandTotal = float(grandTotal)
    grandTotal = round(grandTotal, 2)

    return grandTotal, subTotal, activityFees, totHotelCost, sideTripCost, totGift

def output(totHotelCost, activityFees, sideTripCost, totGift, subTotal,grandTotal, numPeople, beachTrip, tourGuideGifts):
    print('Here\'s your tour estimate!')      #Displays output
    print('{:<20}{:<10}{:>10}{:>8,.2f}'.format(numPeople, 'hotel stay @ $375 each', '$     ', totHotelCost))
    print('{:<20}{:<10}{:>10}{:>8,.2f}'.format(numPeople, 'activity fees @ $150 each', '$      ', activityFees))
    print('{:<20}{:<10}{:>10}{:>8,.2f}'.format(beachTrip, 'side trips @ $100 each', '$     ', sideTripCost))
    print('{:>5}{:>3}{:>8}'.format(tourGuideGifts, '% gift portion ', totGift))
    print('{:<20}{:>3}{:>8,.2f}'.format('subtotal', '$     ', subTotal))
    print('{:<20}{:>10}{:>8,.2f}'.format('Total, excluding air fare', '$', grandTotal))

main()