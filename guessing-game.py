import random

print("Welcome to the guessing game!")
print()
print('In this game you must guess a random number')


ans = random.randrange(101)
response = int[0]
while response != ans:
    print('What is your guess?')
    response = int[input()]
    if response > ans:
        print('Lower')
    elif response < ans:
        print('Higher')

print('Thats Right! You Win!')
