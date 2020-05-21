'''
Jacob Tyson
title: Book List
description: This program obtains user input in inputs function to obtain the number o books the user is getting
then will also obtain the cost of each book and the title of the book. the processing function will give the total amount
and the average cost per book,and finally the outputs function organizes the data by formating it into a nice chart. The
program will be called by running the main() function.
'''

print('This program summarizes a book list.')  # print intro


def main():  # call functions and save results under key variable names.
    try:  # generic exception handling - turn off during development
        num_books, price_list, title = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, total, average, title)
        restart = input('Need more books? Enter y or n: ')  # restart feature
        if restart == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.
        print('Enter the number of books that you need ')  # user sets the list length/ repetitions of the for loop
        num_books = get_pos_int()  # call validation function to collect int > 0
        price_list = []  # create list to save prices
        title = []
        for index in range(num_books):# for loop runs user-specified number of times & collects info on each book
            bookTitles = input(f'please enter the title of book {index + 1}')# obtains book titles
            title.append(bookTitles)#builds title list.
            print(f'Enter the cost of book #{index +1}, to the nearest dollar: ')
            book_cost = get_pos_int()  # call validation function to collect int > 0
            price_list.append(book_cost)  # build price list
        return num_books, price_list, title


def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, total, average, title):  # display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book Title":<10}{"Price":>10}')
    for index in range(len(price_list)):
        for index2 in range(len(title)):
            print('{:<10}{:<10}{:<10}'.format(title[index], '$', price_list[index]))
            break
    print(f'{"Total":<10} ${total:>10.2f}')
    print(f'{"Average":<10} ${average:>10.2f}')


main()  # call main to start or restart program.