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
def main():
    pet = load_pet()
    if pet:
        print(f"\n Welcome Back, {pet.name}!")
    else:
        pet = choose_pet()

    while True:
        pet.decay()
        pet.age_up()

        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Special Action")
        print("5. Pet Status")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.rest()
        elif choice == "4":
            if isinstance(pet, Dog):
                pet.bark()
            elif isinstance(pet, Cat):
                pet.meow()
            elif isinstance(pet, Bunny):
                pet.hop()
            elif isinstance(pet, Panda):
                pet.eat_bamboo()
        elif choice == "5":
            pet.status()
        elif choice == "6":
            save_pet(pet)
            print("Progress saved.")
            break
        else:
            print("Invalid choice.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()