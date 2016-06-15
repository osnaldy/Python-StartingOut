import pickle
import contact

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():

    mycontacts = load_contact()
    choice  = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    save_contacts(mycontacts)

def load_contact():

    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)

        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct

def get_menu_choice():

    print
    print 'Menu'
    print '-------------------------------'
    print '1. Look up a contact'
    print '2. Ad a new contact'
    print '3. Change an existing contact'
    print '4. Delete a contact'
    print '5. Quit the program'
    print

    choice = int(raw_input("Enter you choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(raw_input("Enter a valid choice: "))

    return choice

def look_up(mycontacts):
    name = raw_input('Enter a name: ')
    print

    print mycontacts.get(name, 'That name is not found.')

def add(mycontacts):
    name = raw_input("Name: ")
    phone = raw_input("Phone: ")
    email = raw_input("Email: ")

    entry = contact.Contact(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry
        print "Entry has been added."
    else:
        print "Name already exists."

def change(mycontacts):
    name = raw_input("Enter a name: ")
    if name in mycontacts:
        phone = raw_input("Enter the new Phone Number: ")
        email = raw_input("Enter the new email: ")

        entry = contact.Contact(name, phone, email)

    else:
        print "That name is not found"

def delete(mycontacts):
    name = raw_input("Enter a name: ")

    if name in mycontacts:
        del mycontacts[name]
        print 'Entry delete.'
    else:
        'That name was not found.'

def save_contacts(mycontacts):

    output_file = open(FILENAME, 'wb')

    pickle.dump(mycontacts, output_file)

    output_file.close()

main()