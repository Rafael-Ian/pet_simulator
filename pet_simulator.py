from pet import Dog, Cat, Bunny, Panda, Pet
import json
import os
import time

#Saves the pet's current data to a json file
def save_pet(pet, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(pet.to_dict(), f)

#Loads the pet's data from a file and return the correct pet type
def load_pet(filename="data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            species = data["species"]
            if "Dog" in species:
                return Dog(**data)
            elif "Cat" in species:
                return Cat(**data)
            elif "Bunny" in species:
                return Bunny(**data)
            elif "Panda" in species:
                return Panda(**data)
            else:
                return Pet.from_dict(data)
    return None

#Lets user pick the type of pet they want and choose a name for it
#Main program loop