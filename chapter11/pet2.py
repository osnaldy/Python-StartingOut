import pet

def main():
    name = raw_input("Enter the name of the pet: ")
    animal_type = raw_input("Enter the Type of the animal: ")
    age = raw_input("Enter the age of the pet: ")
    print

    pets = pet.Pet(name, animal_type, age)

    print "Here is the data you have entered"
    print
    print "Name:", pets.get_name()
    print "Type of Animal:", pets.get_animal_type()
    print "Animal's Age:", pets.get_age()

main()