'''
Jacob Tyson
11/14/2019
title: directory_file
description: This program will create a file called usernameEmail.txt. User can choose the options of view or add. The
add option will allow you to append username and emails to the text file.
And the view option will allow you view the current usernames and password that are in the text file.
'''
# Calls the program
def main():
    open('usernameEmail.txt', 'w')
    try:  # Validate user input for commands
        while True:  # loop through commands
            display_menu()
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view()  # calls view function when user issues 'view'
            elif command == 'add':
                add()  # calls add command when user issues 'add'
            elif command == 'exit':
                print('Bye!')
                break  # breaks out of loop when user issues 'exit'
            else:  # validates user command
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')

# allow user to add username and email
def add():
    usernameEmailFile = open('usernameEmail.txt', 'a')  # opens usernameEmail.txt file in append mode

    usernameEmailFile.write(input(f'You have chosen to add new usernames and emails!\n\n'  # gets user input + formats   
                        f'Please use this format:{"." * 20} username email@something.com, username2 email2@something.com'
                        f'\nplease remember to use a comma to separate new contacts!\nTYPE HERE:'))
    usernameEmailFile.close()  # closes usernameEmail.txt file

# allow user to view current username and email
def view():
    usernameEmailFile = open('usernameEmail.txt', 'r')  # opens username.txt in read mode
    readit = usernameEmailFile.readline()  # reads first line of userEmail.txt
    getlist = readit.split(',')  # puts items of string readit into list at each comma
    for i in range(len(getlist)):  # loops through each item in list in getlist
        print(f'({i + 1}): {getlist[i]}')  # prints with format

    usernameEmailFile.close()  # close usernameEmail.txt

# creats display menu
def display_menu():
    print('COMMAND MENU')
    print('view - Username and Email address ')
    print('add - Username and Email address')
    print('exit - Exit program')
    print()
# call program
main()