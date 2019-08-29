#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print('Hello, my name is Caden Mockler')

print('Whats my favorite game?')

print('My favorite game is Fallout: New Vegas')

print('My concern about this class is being unable to keep up or not fulling understanding the lessons.')

print('I am excited to finally be learning coding that will be useful in what I want to do.')

print('My stack overflow number is 11990890')

print('My Github profile url is https://github.com/Caden-Mockler')

answer = input('Is there anything else you would like to know?')
if (answer.lower() == 'yes'):
    print('You will have to talk to real me then, this is just a computer.')
elif (answer.lower() == 'no'):
    print('...ok...I didnt having anything to share anyway.')
else: 
    print('This is really a Yes or No question.')
