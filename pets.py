import json
import os

#Base class for all pets
class Pet:
    def __init__(self, name, species, age=0, hunger=50, energy=50, happiness=50, level=1, experience=0, health=100, evolved=False):
#Person initializes a pet with name, type, and default stats
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.level = level
        self.experience = experience
        self.health = health
        self.evolved = evolved

#Feeds the pet function
def feed(self):
    self.hunger = max(0, self.hunger - 20)
    self.gain_experience(5)
    
#Plays with the pet
#Lets the pet rest and recover energy
#Adds experience points
#Displays the pet's current stats
#Increase the pet's age and checks for evolution
#Evolves the pet if age is 5 or above and not yet evolved
#Evolves the pet, changes its species name, and boost health 
#Apply time-based stat decay for realism
#Converts pet's data to a dictionary for saving
#Loads pet data from dictionary
#Dog subclass with action
#Dog's special action
#Cat subclass with action
#Cat's special action
#Bunny subclass with action
#Bunny's special action
#Panda subclass with action
#Panda's special action

