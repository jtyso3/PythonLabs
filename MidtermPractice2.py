'''
Jacob Tyson
Midterm practice2
This program will determine which english class the student will be placed in based upon their
their reading test score. This uses the mipo style programming framework
'''
def main(): #runs program
    print('Welcome to podunk college:')
    testScore = inputs() #call input function sets return value to variable
    print(f'With a Reading Accuplacer score of {testScore}...') #prints variable above
    englishClass, prepCost, classes = processing(testScore) #call on the processing function, set variables to return values in processing
    output(englishClass, prepCost, classes) #uses return data from processing to compose the output from the output function
    restart = input('Would you like to continue? y or n.')
    if restart == 'y':
        print('OK, let\'s see a new score.')
        main()
    else:
        print('Thanks for using the program.')

def inputs():
    testScore = input('What was your reading test score?') #asks user input for test score.
    testScore = int(testScore) #makes test score become an integer
    while testScore > 120 or testScore <= 0: #validates test score value is an integer between 0 and 120
        testScore = input('Please enter a valid number')
        testScore = int(testScore) #Makes test score into integer.
    return testScore #makes test score availible to call on

def processing(testScore): #based on test score from input funtion, gives data values of english class needed, amount of classes needed, and total cost.
    if testScore < 38:
        englishClass = 'Adult Basic Ed'
        classes = 3
        prepCost = classes * 500
    elif testScore <= 59:
        englishClass = 'READ 100'
        classes = 2
        prepCost = classes * 500
    elif testScore <= 77:
        englishClass = 'READ 200'
        classes = 1
        prepCost = classes * 500
    elif testScore <= 120:
        englishClass = 'College English'
        classes = 0
        prepCost = 0
    return englishClass, prepCost, classes

def output(englishClass, prepCost, classes): #collects data from processing function to display output.
    print('{:<20}{:>10}{:>20}'.format('Your English CLass is', '', englishClass))
    print('{:<20}{:>10}{:<20,.2f}'.format('Your Number of classes Needed:', '#', int(classes)))
    print('{:<20}{:>10}{:<20,.2f}'.format('Prep cost:', '$', prepCost))


main()

