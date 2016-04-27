def main():
    rec = open('record.txt', 'r')

    name = rec.readline()

    while name != '':
        id = rec.readline()

        department = rec.readline()

        name = name.rstrip('\n')
        id = id.rstrip('\n')
        department = department.rstrip('\n')

        #display

        print "Name: ", name
        print 'ID: ', id
        print 'Department:  ', department
        print

        name = rec.readline()
    rec.close()
main()