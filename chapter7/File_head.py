def main():
    file_name = raw_input("Enter the name of the file: ")

    name = open(file_name, 'r')

    for i in range(5):
        number = float(name.readline())
        print number
main()