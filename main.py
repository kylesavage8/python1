import random
import datetime
import os
import sys
import re


class Bird:
    # Make an function for the bird's name and species
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Make a speak function displaying what the bird's name is
    def speak(self):
        print(f"His/Her's name is {self.name}")

    # Make a species function displaying what type of bird species was chosen
    def bird_species(self):
        print(f"This bird's species is a {self.species}")


# Make a species_list for six different types of birds
species_list = ["pigeon", "woodpecker", "bluebird", "northern cardinal", "mousebird", "gannet"]


# Make a species(decision) function
def bird_species(decision):
    while True:
        # Create if elif statements making the user decide what species of bird they want
        if int(decision) == 1 or str(decision) == "pigeon":
            return "pigeon"
        elif int(decision) == 2 or str(decision) == "woodpecker":
            return "woodpecker"
        elif int(decision) == 3 or str(decision) == "bluebird":
            return "bluebird"
        elif int(decision) == 4 or str(decision) == "northern cardinal":
            return "northern cardinal"
        elif int(decision) == 5 or str(decision) == "mousebird":
            return "mousebird"
        elif int(decision) == 6 or str(decision) == "gannet":
            return "gannet"
        else:
            decision = input("Input the species number: ")


if __name__ == '__main__':
    # Print the name of the first bird
    b1_name = input("Bird ones name is: ")
    # Print the name of the second bird
    b2_name = input("Bird two's name is: ")
    # Print if the computer selects a species randomly for b1
    random_decision = input("Decision for computer to select a species randomly for b1 (y/n): ")
    # Make an if else statement for selected b1
    if random_decision.lower() == "y":
        b1 = Bird(b1_name, random.choice(species_list))
    else:
        # Print the species list
        print("Now print the species list:")
        for num, i in enumerate(species_list):
            print(num + 1, i)
        # Print a species or number
        selected_species = input("Input the species number: ")
        b1_species = bird_species(selected_species)
        b1 = Bird(b1_name, b1_species)
    # Print if the computer selects a species randomly for b2
    random_decision = input("Decision for computer to select a species randomly for b2 (y/n): ")
    # Make an if else statement for selected b2
    if random_decision.lower() == "y":
        b2 = Bird(b2_name, random.choice(species_list))
    else:
        print("Now print the species list:")
        for num, i in enumerate(species_list):
            print(f" {num + 1}", i)
        # Print a species or number
        selected_species = input("Input the species number: ")
        b2_species = bird_species(selected_species)
        b2 = Bird(b2_name, b2_species)

    # Print that two birds have been created
    print("Two birds have been created")
    # Print that you created the first bird
    print("First bird is:")
    b1.speak()
    b1.bird_species()
    # Print that you created the second bird
    print("Second bird is:")
    b2.speak()
    b2.bird_species()
    # Display both all the methods and attributes
    attribute = dir(Bird)
    methods = []
    attributes = []

    # Make a for loop displaying all the methods and attributes
    for i in attribute:
        if i.startswith("__"):
            attributes.append(i)
        else:
            methods.append(i)
    # Print the total attributes
    print(f"Total attributes are: {attributes}")
    # Print the total methods
    print(f"Total methods are: {methods}")
