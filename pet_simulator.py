from pet import Dog, Cat, Bunny, Panda, Pet
import json
import os
import time

#Saves the pet's current data to a json file
def save_pet(pet, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(pet.to_dict(), f)
        
#Loads the pet's data from a file and return the correct pet type
#Lets user pick the type of pet they want and choose a name for it
#Main program loop