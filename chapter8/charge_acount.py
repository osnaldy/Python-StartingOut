def main():
    file_name = open('charge_account.txt','w')
    again = 'y'

    while again == 'y':
        number = int(raw_input("Enter the number to be added to the file: "))
        file_name.write(str(number) + '\n')
        again = raw_input("Enter 'y' to continue, anything else to stop ")
    file_name.close()
main()