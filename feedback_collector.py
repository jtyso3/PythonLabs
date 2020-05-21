'''
Jacob Tyson
Title: Feedback Collector
Description: This program will allow gather user input on feedback phrases, and then print them out for viewing pleasure.
'''
def main():             #calls the program
    phrases = inputs() #gets phrases variable from inputs()
    list2 = processing(phrases) #gets list2 by using phrases
    outputs(list2) #formats list2


def inputs():
    print('Please enter multiple feedback phrases, each ending in a !') #intro statement
    phrases = input('Please enter as many as you like. You don\'t have to capitalize') #gets user input
    while phrases.isnumeric() or phrases == '' or phrases.isspace() or '!' not in phrases: #Validates user input
        phrases = input('Please remember to use an \'!\' after every phrase')


    return phrases        #makes unser input available

def processing(phrases):                    #gets phrases, puts into list, puts list into new list, corrects new list
    list1 = phrases.split('!')    #seperates string by !, creates list
    list1.pop() #gets rid of extra list values
    list2 = [] #new list

    for index2 in range(len(list1)): #gets lists values
        list2.append(list1[index2].strip().capitalize() + '!') #puts list into new list, corrects user errors.

    return list2 #makes new list available

def outputs(list2):
    for index3 in range(len(list2)): #gets list2 values
        print(f'{index3 + 1}: {list2[index3]}') #formats list2 values to print

main()
