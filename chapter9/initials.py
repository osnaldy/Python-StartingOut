def main():
    first = raw_input("Enter the first name: ")
    middle = raw_input("Enter the middle name: ")
    last = raw_input("Enter the last name: ")
    print first[0:2] + '.' + middle[0:2] + '.' + last[0:2]
main()