'''
Jacob Tyson
11/27/2019
csv_read.py
This program will open a csv file read it and then display it.
'''
import csv
example_file = open('lab.csv', encoding='utf-8')  # opens the csv file
example_reader = csv.reader(example_file)  # reads csv file, by every line
print('Here is Lab.csv!!!!!!!')
for row in example_reader:  # loops through every line in csv file
	print('{:<18} {:^18} {:>5}'.format(*row, end=''))  # prints each row, in table fashion