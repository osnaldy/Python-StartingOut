def main ():

    number = int(raw_input("Enter the number of employees to create records for : "))

    rec = open('record.txt', 'w')

    for i in range(1, number + 1):
        print "Enter the information for employee #", i
        name = raw_input('Name: ')
        id = raw_input("Enter the ID #: ")
        department = raw_input("Enter the Department name")

        rec.write(name + '\n')
        rec.write(id + '\n')
        rec.write(department + '\n')
        print

    rec.close()

    print "Record of employees have been added to file"

main()