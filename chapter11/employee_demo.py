import pickle
import json
import employee

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILE = 'employees.dat'

def main():

    employees = load_file()
    choice = 0

    while choice != QUIT:
        choice = choices()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

        saveinfo(employees)

def load_file():

    try:
        input_file = open(FILE, 'rb')
        employee_dict = pickle.load(input_file)
        input_file.close()

    except IOError:
        employee_dict = {}

    return employee_dict
def choices():

    print
    print 'Menu'
    print '-------------------------------'
    print '1. Look up an employee'
    print '2. Ad a new employee'
    print '3. Change an existing employee'
    print '4. Delete an employee'
    print '5. Quit the program'
    print

    choice = int(raw_input('Enter a choice to follow up: '))

    while choice < 0 or choice > 5:
        choice = int(raw_input("Enter the choice again: "))

    return choice

def look_up(employees):

    id = raw_input("Enter the ID_number of the employee: ")
    print

    print employees.get(id, 'Not Found!')

def add(employees):

    name = raw_input("Enter the name of the employee: ")
    id = raw_input("Enter the ID_number of the employee: ")
    department = raw_input("Enter the department for which the employee works for: ")
    job_title = raw_input("Enter the employee's Job Title: ")

    entry = employee.Employee(name, id, department, job_title)

    if id not in employees:
        employees[id] = entry
        print 'Employee has been added'
    else:
        print 'Employee already exists'

def change(employees):

    id = raw_input("Enter the employee's ID_number to change information: ")

    if id in employees:
        name = raw_input("Enter the name of the employee: ")
        department = raw_input("Enter the department for which the employee works for: ")
        job_title = raw_input("Enter the employee's Job Title: ")

        entry = employee.Employee(name, id, department, job_title)

    else:
        print "Employee's ID_number not Found!"

def delete(employees):

    id = raw_input("Enter the employee's ID_number to delete information")

    if id in employees:
        del employees[id]
        print 'Employee has been delete'
    else:
        print 'Employee ID_number does not exist!'

def saveinfo(employees):

    out_put = open(FILE, 'wb')

    pickle.dump(employees, out_put)

    out_put.close()

main()
