REGULAR_HOURS = 40
OVERTIME = 1.5

def main():
    hours_worked = float(raw_input("Enter the hours worked: "))
    pay_rate = float(raw_input("Enter the pay rate: "))

    if hours_worked > REGULAR_HOURS:
        overtime(hours_worked, pay_rate)
    else:
        regulartime(hours_worked, pay_rate)

def overtime(hours, pay):
    overtime_time = hours - REGULAR_HOURS
    pays = overtime_time * pay * OVERTIME
    total = REGULAR_HOURS * pay + pays
    print "Your total gross pay is", format(total, '.2f')

def regulartime(hours, pay):
    total = hours * pay
    print "Your total gross pay is", format(total, '.2f')
main()