'''
Jacob Tyson
Title: web_scraping1
Description: This program will get the text file from the web page, and then print it to the console.
'''
import requests

file = requests.get('https://www.gutenberg.org/files/20203/20203-8.txt')  # Gets text file
print(file.text)  # prints entire text File.