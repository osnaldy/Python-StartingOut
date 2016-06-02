import pickle

def main():

    again = 'y'
    output = open('info.dat','wb')
    while again.lower() == 'y':
        save_data(output)
        again = raw_input("Enter more data? (y/n): ")
    output.close()


def save_data(file):

    person = {}

    person['name'] = raw_input("Enter the person's name: ")
    person['age'] = raw_input("Enter the person's age: ")
    person['weight'] = raw_input("Enter the person's weight: ")

    pickle.dump(person, file)
main()