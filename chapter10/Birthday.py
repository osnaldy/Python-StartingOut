LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    birthdays = {}
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

def get_menu_choice():
    print '-----------------------'
    print '1. Look up a birthday '
    print '2. Add a birthday '
    print '3 Change a birthday '
    print '4. Delete a birthday '
    print '5. Quit the program '
    print

    choice = int(raw_input("Enter the a number for your choice "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(raw_input("Enter a value choice: "))
    return choice

def look_up(birthdays):
    name = raw_input("Enter the name to look up: ")
    print birthdays.get(name, 'Not found.')

def add(birthdays):
    name = raw_input("Enter the name: ")
    bday = raw_input("Enter the birthday: ")

    if name not in birthdays:
        birthdays[name] = bday
    else:
        print "Entry already exists.!"

def change(birthdays):
    name = raw_input("Enter a name to look up")

    if name in birthdays:
        bday = raw_input("Enter the new birthday: ")
        birthdays[name] = bday
    else:
        print "Name not Found!"
def delete(birthdays):
    name = raw_input("Enter the a name to delete")
    if name in birthdays:
        del birthdays[name]
    else:
        print "That Name is not found!!"
main()