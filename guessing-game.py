# 1. Name:
#      M. Scott O'Connor
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      A game where the user has to guess a number between 1 and a user specified upper bound
# 4. What was the hardest part? Be as specific as possible.
#      This was my first time using python, so the hardest part was getting the syntax right.
#      In general it was actually simpler than the C based languages that I am used to, but
#      it still isn't what I'm used to. I had particular trouble with the automatic assignment 
#      of variable types as the input for the guesses defaulted to strings and it wouldn't let 
#      me compare with the integer answer. Second would be the fact that I could not declare a 
#      variable inside a loop, but had to do so before hand. As far as the problem itself goes,
#      I felt it was rather simple. Once I got the syntax correct there were no crashes or 
#      unexpected outputs or any other kinds of bugs. Everything worked as expected. My biggest 
#      issue was deciding if I wanted to include the user's upper bound in the possible answers 
#      or not as I could not find a section in the assignment that specified explicitly. However, 
#      I discovered that the first test case would not work without including the upper bound.
# 5. How long did it take for you to complete the assignment?
#      2.5 hrs

import random
#Intro
print("Welcome to the number guessing game!")
print('In this game you must guess a random number\n')

upperBound = int(input('Pick a positive whole number: '))

while upperBound < 1:
    upperBound = input('Invalid input! Please enter a positive whole number: ')

# Determines that greatest number allowed
print('Guess a number between 1 and', upperBound)
ans = random.randrange(1, upperBound + 1)

response = -1

guessList = list()

# Main Game play Loop
while response != ans:
    response = int(input('> '))
    guessList.append(response)
    
    if response < 1 or response > upperBound:
        print('\tAnswer out of bounds')
    elif response > ans:
        print('\tTry Lower')
    elif response < ans:
        print('\tTry Higher')

# Win Message
print('Thats Right! You Win!\n')
print('You got it in', len(guessList), "guesses.")
print('Your guesses:', guessList)
