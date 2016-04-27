import os
def main():
    found = False
    coffee = open('coffee.txt', 'r')

    temp = open('tempo.txt', 'w')

    search = raw_input("Enter the description to see if it matches: ")
    new_quantity = float(raw_input("Enter the new quantity to be modify: "))

    description = coffee.readline()

    while description != '':
        quantity = float(coffee.readline())
        description = description.rstrip('\n')

        if description == search:
            temp.write(description + '\n')
            temp.write(str(new_quantity) + '\n')
            found = True
        else:
            temp.write((description + '\n'))
            temp.write(str(quantity)+ '\n')
        description = coffee.readline()
    coffee.close()
    temp.close()

    os.remove('coffee.txt')
    os.rename('tempo.txt', 'coffee.txt')

    if found:
        print "File has been updated"
    else:
        print "That item was not found in the file"

main()
