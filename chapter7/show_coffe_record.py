def main():
    coffee = open('coffee.txt', 'r')

    description = coffee.readline()

    while description != '':
        quantity = float(coffee.readline())

        description = description.rstrip('\n')

        print "Description: ", description
        print "Quantity: ", quantity
        print
        description = coffee.readline()

    coffee.close()
main()