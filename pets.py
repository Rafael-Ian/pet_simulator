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
def play(self):
    if self.energy >= 20:
        self.happiness = min(100, self.happines + 15)
        self.energy -= 20
        self.hunger = min(100, self.hunger + 10)
        self.gain_experience(10)
    else:
        print(f"{self.name} is too tired to play.")

#Lets the pet rest and recover energy
def rest(self):
    self.energy = min(100, self.energy + 30)
    self.hunger = min(100, self.hunger + 10)
    self.gain_experience(5)

#Adds experience points
def gain_experience(self, amount):
    self.experience += amount
    if self.experience >= 100:
        self.level += 1
        self.experience = 0
        print(f"Congratulations {self.name} leveled up to Level {self.level}!!")
#Displays the pet's current stats
def status(self):
    print(f"\n--- {self.name}'s Status ---")
    print(f"Species: {self.species}")
    print(f"Age: {self.age}")
    print(f"Level: {self.level}")
    print(f"HP: {self.level}/100")
    print(f"Hunger: {self.hunger}/100")
    print(f"Energy: {self.energy}/100")
    print(f"Happiness: {self.happiness}/100")

#Increase the pet's age and checks for evolution
def age_up(self):
    self.age += 1
    print(f"\n {self.name} is now {self.age} years old!")
    self.check_evolution()

#Evolves the pet if age is 5 or above and not yet evolved
def check_evolution(self):
    if not self.evolved and self.age >= 5:
        self.evolve()

#Evolves the pet, changes its species name, and boost health
def evolve(self):
    self.evolved = True
    self.species += "(Evolved)"
    self.health = min(100, self.health + 20)
    print(f" {self.name} has evolved into a stronger {self.species}!")

#Apply time-based stat decay for realism
def decay(self):
    self.hunger = min(100, self.hunger + 5)
    self.energy = max(0, self.energy - 5)
    self.happiness = max(0, self.happiness - 2)
    self.health = max(0, self.health - (self.hunger // 30))

#Converts pet's data to a dictionary for saving
def to_dictionary(self):
    return {
        "name": self.name,
        "species": self.species,
        "age": self.age,
        "hunger": self.hunger,
        "energy": self.energy,
        "happiness": self.happiness,
        "level": self.level,
        "experience": self.experience,
        "health": self.health,
        "evolved": self.evolved
    }
@classmethod
#Loads pet data from dictionary
def from_dictionary(cls,data):
    return cls(
        data["name"]
        data["species"]
        data["age"]
        data["hunger"]
        data["energy"]
        data["happiness"]
        data["level"]
        data["experience"]
        data["health"]
        data.get("evolved", False)
    )

#Dog subclass with action
class Dog(pet):
    def __init__(self, name, **kwargs):
        super().__init__(name, "Dog", **kwargs)

#Dog's special action
    def bark(self):
        print(f"{self.name} barks: Woof!")
        self.happiness = min(100, self.happiness + 5)
        self.gain_experience(3)
        
#Cat subclass with action
#Cat's special action
#Bunny subclass with action
#Bunny's special action
#Panda subclass with action
#Panda's special action

