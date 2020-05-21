'''
Jacob Tyson
11/14/2019
'''
import os
print('Creating new directory folders.')
my_path = os.getcwd()	# save current working directory under variable name
print(my_path)
print('Create a new directory: test_dir')
#os.makedirs(my_path+'/test_dir')  # OSX or Linux
os.makedirs(my_path+r'\test_dir')  # Windows
print('OK I think that worked – check directory to see new folder.')
print('If so, comment out the line that worked – only usable once.')