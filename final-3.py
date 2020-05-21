

def main():
    while True:
        print('Please enter a command:\ncreate csv: (creates csv file, WARNING saved data will erase\n add: to add more data to csv\n exit:')
        command = input('COMMAND:')
        while command.isspace() or command.isnumeric() or command == '':
            command = input('please enter a valid command.')
        command = command.lower()
        if command == 'add':
            sqft, gallons = add()
        elif command == 'create csv':
            createCsv()
        elif command == 'view':
            view(sqft, gallons)
        elif command == 'exit':
            break

def add():
    example_file = open('final.csv', 'a')
    list1 = []
    room = input('Room Initials:')
    while room.isnumeric() or room.isspace():
        room = input('please use a whole number less than or equal to 5, ex. 4:')

    color = input('Room Color:')
    while color.isnumeric() or color.isspace():
        color = input('please use a whole number less than or equal to 5, ex. 4:')

    length = input('Room length:')
    while length.isalpha():
        length = input('please use a whole number less than or equal to 5, ex. 4:')
    length = int(length)

    width = input('Room length:')
    while width.isalpha():
        width = input('please use a whole number less than or equal to 5, ex. 4:')
    width = int(width)

    hieght = input('Room length:')
    while hieght.isalpha():
        hieght = input('please use a whole number less than or equal to 5, ex. 4:')
    hieght = int(hieght)

    list1.append(room)
    list1.append(color)
    list1.append(str(length))
    list1.append(str(width))
    list1.append(str(hieght))


    sqft = length * width
    sqft= str(sqft)
    gallons = length * width * hieght
    gallons = str(gallons)
    list1.append(sqft)
    list1.append(gallons)
    string1 = ' '
    for i in list1:
        example_file.write(i)
        example_file.write('\n')

    example_file.close()

    return sqft, gallons

def view(sqft, gallons):
    example_file = open('final.csv', 'r')  # opens ratingsfile.txt in read mode
    read_file = example_file.readlines()  # reads first line of ratingsfile.txt
     # puts items of string readit into list at each comma

    print('{:<10}{:>10}{:>10}{:>15}{:>10}{:>10}{:>10}'.format('Room', 'Color', 'Length', 'Width', 'Hieght', 'Sq. Ft.', 'Gallons'))
    print('{:<3}{:>11}{:>15}{:>10}{:>15}{:>10}{:>10}'.format(read_file[0], read_file[1], read_file[2], read_file[3], read_file[4],sqft, gallons))

main()