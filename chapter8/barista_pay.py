employee = 6
def main():
    hours = [0] * employee

    for index in range(employee):
        hours[index] = float(raw_input("Enter the hours worked by employee #" + str(index+1) + ': '))

    pay_rate = float(raw_input("Enter the Pay Rate: "))
    total = 0
    for index in range(employee):
        gross_pay = hours[index] * pay_rate
        total += gross_pay
        print "Gross Pay for employee #", index + 1, 'is :', format(gross_pay, ',.2f')
    print
    print "The sum pay to all employee totaled", total



main()