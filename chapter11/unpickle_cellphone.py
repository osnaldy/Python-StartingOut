import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():

    end_file = False

    input_file = open(FILENAME, 'rb')

    while not end_file:
        try:
            phone = pickle.load(input_file)

            display_data(phone)

        except EOFError:
            end_file = True
    input_file.close()

def display_data(phone):

    print "Here is the Data you saved in you file "
    print
    print "Manufacturer:", phone.get_manufact()
    print "Model Number:", phone.get_model()
    print "Retail Price:", phone.get_retail_price()

main()