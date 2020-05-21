'''
Jacob Tyson
11/30/2019
data_collection.py
This program will create a csv file that will store contact information that the user will add by using the program.
User will have the options to add contacts of view contacts.
'''
import csv

def main():
    print('COMMAND MENU')
    print('view - Display contact information')
    print('add - Create new contact')
    print('exit - Exit program')

    create_file = open('usernameEmail.csv', 'w', newline='')  # create file in write mode
    heading = csv.writer(create_file)  # create a Writer object
    heading.writerow(['Name', 'Email', 'Phone'])  # Creates Heading
    create_file.close()

    try:  # Validate user input for commands
        while True:  # loop through commands, until exit is called
            add_file = open('usernameEmail.csv', 'a', newline='')  # open file in append mode
            read_file = open('usernameEmail.csv', encoding='utf-8')  # open file in read mode

            command = input('Command: ')  # gets user command
            command = command.lower()  # accounts for case sensitivity
            if command == 'view':
                view(read_file)  # calls view function when user issues 'view'
                read_file.close()
            elif command == 'add':
                add(add_file)  # calls add command when user issues 'add'
                add_file.close()
            elif command == 'exit':
                create_file.close()  # close file
                print('Bye!')
                break  # breaks out of loop when user issues 'exit, ends program'
            else:  # validates user command
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')
    return add_file, read_file
# allow user to add username and email

def add(add_file):  # add to end of file

    userInput = input(f'You have chosen to add new contact information!\n\n'  # gets user input + formats   
                        f'Please use this format:{"." * 20} name, email@something.com (email), 232-432-5553 (phone number)'
                        f'\nplease remember to use a comma to separate new contacts!!!!\nTYPE HERE:')
    makeList = userInput.split(',')  # makes user input into list, from comma.
    writethis = csv.writer(add_file)  # appends user input into file
    writethis.writerow(makeList)  # adds list info into csv file


# allow user to view current username and email
def view(read_file):  # open file in read mode
    reader = csv.reader(read_file)  # reads csv file line
    for row in reader:
        print('{:<18} {:^18} {:>5}'.format(*row, end=''))  # creates display of lines in csv file
# call program
main()