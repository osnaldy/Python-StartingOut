def main():
    found = False

    search = raw_input("Enter the description to see if it matches: ")
    coffee = open('coffee.txt', 'r')

    description = coffee.readline()

    while description != '':
        quantity = float(coffee.readline())

        description = description.rstrip('\n')

        if description == search:
            print "Description:", description
            print "Quantity:", quantity
            print
            found = True

        description = coffee.readline()
    coffee.close()

    if not found:
        print "Sorry file could'nt be found"
main()