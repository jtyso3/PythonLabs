'''
Jacob Tyson
10/10/2019
Title: username_fullname
Description: This program will allow you to add, edit, view and delete users and their names from a dictionary.

'''

def main():      #Calls program
    try:
        users = {'jtyson': 'Jake Tyson', 'ugrant': 'Ulysess Grant', 'jcesar': 'julius Cesar'}
        while True:
            display_menu()
            command = input('Command: ')
            command = command.lower()
            if command == 'view':
                view(users)
            elif command == 'add':
                add(users)
            elif command == 'exit':
                print('Bye!')
                break
            elif command == 'del':
                delete(users)
            elif command == 'edit':
                edit(users)
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():  # Displays user command menu
    print('COMMAND MENU')
    print('view - View username')
    print('add - Add a username')
    print('del - Delete a username')
    print('edit- Edit a username')
    print('exit - Exit program')
    print()


def view(users): #Gives names of users, and view book titles with users
    display_codes(users)
    user_code = input('Enter Username to view: ')
    user_code = user_code.lower()
    if user_code in users:
        user_code = users[user_code]
        print('Username name: ' + user_code + '.\n')
    else:
        print('There is no no one without a username. \n')


def add(users): #Adds Users
    display_codes(users)
    name_code = input('Enter new username to add: ')
    name_code = name_code.lower()
    if name_code in users:
        user_name = users[name_code]
        print(user_name + ' is already using this code. \n')
    else:
        user_name = input('Please enter First and Last Name: ')
        user_name = user_name.title()
        users[name_code] = user_name
        print(user_name + ' was added. \n')


def delete(users): #Allows aurthor to delete users
    display_codes(users)
    user_code = input('Enter username to delete: ')
    user_code = user_code.lower()
    if user_code in users:
        user_name = users.pop(user_code)
        print(user_name + ' was deleted. \n')
    else:
        print('There is no user with that username. \n')

def edit(users): #lets you delete, and then add a user
    display_codes(users)  # provides authors name in library
    user_code = input('Enter Username to edit: ')  # Enter new author name
    user_code = user_code.lower()
    if user_code in users:  # Adds author to dictionary
        user_name = input('Enter new Name: ')  # validation
        user_name = user_name.title()
        users[user_code] = user_name
        print(user_name + ' was added. \n')

def display_codes(users): #displays users, key of dictionary
    user_codes = list(users.keys())
    user_codes.sort()
    line = 'Usernames: '
    for user_codes in user_codes:
        line += user_codes + ' '
    print(line)


if __name__ == '__main__':
    main()
