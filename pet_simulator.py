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
def choose_pet():
    name = input("Name your pet: ")
    print("Choose a species: \n1. Dog\n2. Cat\n3. Bunny\n4. Panda")
    choice = input("Enter choice: ")
    if choice == "1":
        return Dog(name)
    elif choice == "2":
        return Cat(name)
    elif choice == "3":
        return Bunny(name)
    elif choice == "4":
        return Panda(name)
    else:
        print("Invalid species. Defaulting to Dog.")
        return Dog(name)
    
#Main program loop