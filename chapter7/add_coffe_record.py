def main():
    # Variable to control the loop
    var = 'y'
    coffees = open('coffee.txt', 'a')

    while var == 'y' or var == 'Y':
        print "Enter the data to be added to the file:"
        description = raw_input("Enter the description of the coffee: ")
        quantity = int(raw_input("Enter the quantity of the coffee: "))

        coffees.write(description + '\n')
        coffees.write(str(quantity) + '\n')

        var = raw_input('Y = yes, anything else = no: ')

    coffees.close()
    print 'Data has been appended to the file'


main()
