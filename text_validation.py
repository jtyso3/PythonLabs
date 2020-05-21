'''
Jacob Tyson
10/31/2019
Title: Name spell check
Description: This program will ask user for a name. Then corrects the name with proper capitalization and spacing.

'''

def main():                     #calls program
    string = processing()       #gets string from
    print('The full name corrected is: ' + string)        #prints string from processing


def processing():
    name = input('Please enter a name for validation and correction')     #obtains users name
    while name.isnumeric() or name == '' or name.isspace():                                  #validates users name
        name = input('Please try again, enter a full name.')

    namelist = name.split()                     #Puts user input in list at space.
    newNameList = []
    for index in range(len(namelist)):                          #runs through name list
        newNameList.append(namelist[index].capitalize().strip())           # adds lists to new list in-order too get rid of capital letters and spaces

    string = ' '                                                #blank string
    for index2 in range(len(newNameList)):                      #adds new list into blank string
        string = string + newNameList[index2] + ' '

    return string                                                #returns string

main()                      #calls function

