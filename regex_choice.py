'''
Jacob Tyson
11/07/2019
Title: random facts about Cant't stop
description: This program uses regex to match and find patterns throughout the song can't stop. Then will print a
numerical fact found about each of the regex created.
'''

import re
cantStopLyrics = '''Can't stop, addicted to the shindig
Chop Top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunct the pistol that you pay for
This punk, the feeling that you stay for
In time I want to be your best friend
East side lovers living on the west end
Knocked out but boy you better come to
Don't die, you know the truth as some do
Go write your message on the pavement
Burn so bright I wonder what the wave meant
White heat is screaming in the jungle
Complete the motion if you stumble
Go ask the dust for any answers
Come back strong with fifty belly dancers
The world I love
The tears I drop
To be part of
The wave, can't stop
Ever wonder if it's all for you?
The world I love
The trains I hop
To be part of
The wave, can't stop
Come and tell me when it's time to'''

print('Here are some random facts about the song Can\'t Stop by the Red Hot Chili Peppers?')

compiler1 = re.compile(r'.at') #matches every word with at
one = compiler1.findall(cantStopLyrics)
for index in range(len(one)): #counter
    index+= 1
print(f'There are {index} amount of words that contain.............\'at\'')

compiler2 = re.compile(r'can\'t|Can\'t')#finds the word can't
two = compiler2.findall(cantStopLyrics) #puts matched patterns is a list
for index in range(len(two)): #counter
    index= index + 1
print(f'There are {index} amount of the word:......................"can\'t"')

compiler3 = re.compile(r'[a-zA-Z]$' )#finds the last character of the songs lyric
three = compiler3.search(cantStopLyrics)
print(f'The last character in the song is..........................{three.group()}')


compiler4 = re.compile(r'.\'') #Finds words with "
four = compiler4.findall(cantStopLyrics)
print(four)
for index in range(len(four)): #counter
    index = index + 1
print(f'There are {index} amount of words with:...........................\'')

compiler5 = re.compile(r'(^\w)')#Finds first character of string.
five = compiler5.search(cantStopLyrics)
print(f'This is the first character of the string:.................{five.group()}')

compiler6 = re.compile(r'([\w\'-]+)')#Gets every word
six = compiler6.findall(cantStopLyrics)
for index in range(len(six)): #counter
    index += 1
print(f'The total amount of lyrics in the song are:................{index}')

compiler7 = re.compile(r'^([\w\'-]+)')#gets first word
seven = compiler7.search(cantStopLyrics)
print(f'This is the first word of the song:........................{seven.group()}')

compiler8 = re.compile(r'((.*\n))' )#get white space including new lines, use to count lines
eight = compiler8.findall(cantStopLyrics)
for index in range(len(eight)): #counter
    index += 1
print(f'There are a total line count of............................{index}')


compiler9 = re.compile(r'\b')#measure amount of spaces
nine = compiler9.findall(cantStopLyrics)
for index in range(len(nine)): #counter
    index += 1
print(f'There is a total space count of:...........................{index} ')

compiler10 = re.compile(r'[AEIOUaeiou]')#gets vowels cap or lower
ten = compiler10.findall(cantStopLyrics)
for index in range(len(ten)): #counter
    index += 1
print(f'There are a total vowel count of:..........................{index} ')

