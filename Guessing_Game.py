from random import randint
from time import sleep

print('Hi i am a computer and i go choose a number between 0 and 20, try guess witch one')

print(40 * "-=")

print('Chossing...')

sleep(2)

Aleatory = randint(0,20)

print(15 * "-=")

Player_Choose = int(input('Try guess witch number chosse: '))

while Player_Choose != Aleatory:

    print("Wrong, Try again")

    print(10 * "-=")

    Player_Choose = int(input('Try guess witch number chosse: '))

print(20 * "-=")

print(f"Correct Answer i guess {Aleatory} and you chosse {Player_Choose}")