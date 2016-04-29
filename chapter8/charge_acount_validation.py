def main():
    #Here we open the file and read the lines
    file_name = open("charge_account.txt", 'r')
    charges = file_name.readlines()
    file_name.close()

    #Here we create an empty array, loop through it and append the values to a list
    arr = []
    for i in charges:
        name = int(i)
        arr.append(name)

    #Here we verify if the value searched in the list exists
    search = int(raw_input("Enter the number to be searched: "))
    if search in arr:
        print "Valid number"
    else:
        print "Invalid number"
main()