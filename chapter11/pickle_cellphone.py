import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():
    again = 'y'

    output = open(FILENAME, 'wb')

    while again.lower() == 'y':
        man = raw_input("Enter the manufacturer: ")
        mod = raw_input("Enter the model number: ")
        retail = float(raw_input("Enter the retail price: "))

        phone = cellphone.Cellphone(man, mod, retail)

        pickle.dump(phone, output)

        again = raw_input("Enter more data y/n ?: ")

    output.close()

    print 'The Data was written to', FILENAME
main()