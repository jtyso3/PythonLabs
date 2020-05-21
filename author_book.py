'''
Jacob Tyson
10/10/2019
Title: author and book tracker program
Description: This program will use and add, edit, delete, and view feature to keep track of you library!
'''
import pprint
def main(): #Runs the program
    try:
        authors_book ={'George R.R. Martain': 'A Game Of Thrones',   #dictionary of author (key) and books(value)
                       'J.K. Rolling': 'Harry Potter',
                       'J.R.R Tolkien': 'Lord Of the Rings'}
        while True:
            display_menu()                #calls command menu
            command = input('Command: ')    #gets users command
            command = command.lower()
            if command == 'view':             #user commands
                view(authors_book)
            elif command == 'add':
                add(authors_book)
            elif command == 'exit':              #stops program
                print('Bye!')
                break
            elif command == 'del':
                delete(authors_book)
            elif command == 'edit':
                edit(authors_book)
            elif command == 'show library':
                table(authors_book)
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():                             #Gives command options.
    print('COMMAND MENU')
    print('view - View Author name')
    print('add - Add a Author')
    print('del - Delete a Author')
    print('edit - edits author books')
    print('exit - Exit program')
    print('show library - displays author and books')
    print()


def view(authors_book):                                               #View option
    display_codes(authors_book)                                           #provides authors names in library(keys)
    author_code = input('Enter Author to view book titles: ')         #Asks authors
    author_code = author_code.title()
    if author_code in authors_book:                                   #Gives authors book titles(values)
        BookTitle = authors_book[author_code]                       #calls for values
        print('Book Title: ' + BookTitle + '.\n')                  #prints values
    else:
        print('There is no Author with that name. \n')              #validation


def add(authors_book):                                                  #adds author and book titles
    display_codes(authors_book)                                            #provides authors name in library
    author_code = input('Enter new Author Name to add: ')                  #Enter new author name
    author_code = author_code.title()                                       #accounts for case sensitivity
    if author_code in authors_book:                                     #Adds author to dictionary
        author_name = authors_book[author_code]
        print(author_name + ' is already using this code. \n')
    else:
        author_name = input('Enter Book Title: ')                       #validation
        author_name = author_name.title()
        authors_book[author_code] = author_name
        print(author_name + ' was added. \n')

def delete(authors_book):                                           #Deletes authors
    display_codes(authors_book)
    author_code = input('Enter Author to delete: ')                  #User input for author deleted
    author_code = author_code.title()                                 #acounts for case sensitivity
    if author_code in authors_book:                                  #Deletes author
        author_name = authors_book.pop(author_code)
        print(author_name + ' was deleted. \n')
    else:
        print('There is no Author with that name. \n')

def edit(authors_book):                                         #Uses delete() and add() to work as an edit feature
    display_codes(authors_book)  # provides authors name in library
    author_code = input('Enter author Name to edit: ')  # Enter new author name
    author_code = author_code.title()
    if author_code in authors_book:                                     #Adds author to dictionary
        author_name = input('Enter new book title: ')                       #validation
        author_name = author_name.title()
        authors_book[author_code] = author_name
        print(author_name + ' was added. \n')

def table(authors_book):
    print('Here is a nice display of your library!')
    for display in authors_book:
        print(display + '\t' + '\t' + authors_book[display])


def display_codes(authors_book):                                 #provides list of authors in dictionary
    Author_codes = list(authors_book.keys())
    Author_codes.sort()
    line = 'Authors: '
    for Author_codes in Author_codes:
        line += Author_codes + ' '
    print(line)
if __name__ == '__main__':
    main()


