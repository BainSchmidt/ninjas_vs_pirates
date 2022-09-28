import random
from re import M
from urllib import response
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")
jack_sparrow.show_stats()
michelangelo.show_stats()

print("Welcome to Ninjas vs Pirates!")
while( michelangelo.health > 0 and jack_sparrow.health >0):
    response =""
    while not response == "1" and not response == "2" and not response == "3":
        if michelangelo.rum > 0:
            print("Ninja get ready! Whats your next move? \n 1)attack \n 2)Take rum \n 3)Drink rum")
        else:
            print("Ninja get ready! Whats your next move? \n 1)attack \n 2)Take rum")
        response = input (">>>")
        if response == "1":
            michelangelo.attack(jack_sparrow)
        elif response == "2":
            michelangelo.take_rum(jack_sparrow)
        elif response == "3":
            michelangelo.ninja_drink_rum()
        else:
            print("Quit messing around, type a valid option! >:(")

        pirate_action = random.randint(1,2)
        if response == "1":
            jack_sparrow.attack(michelangelo)
            print(pirate_action) # testing
        elif response == "2":
            print(pirate_action) # testing
            jack_sparrow.drink_rum()
        
if jack_sparrow.health <= 0:
    print(f"You have defeated {jack_sparrow}")
if michelangelo.health <= 0:
    print(f"You have fallen to your death")