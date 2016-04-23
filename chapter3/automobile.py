def main():
    expense()

def expense():
    loan = float(raw_input("Enter the loan payment: "))
    insurance = float(raw_input("Enter the insurance payment: "))
    gas = float(raw_input("Enter the gas payment: "))
    oil = float(raw_input("Enter the oil payment: "))
    tires = float(raw_input("Enter the tire payment: "))
    maintenace = float(raw_input("Enter the maintenance payment: "))

    monthly  = (loan+insurance+gas+oil+tires+maintenace)

    print "The monthly cost is", monthly

    yearly = monthly * 12

    print "The yearly cost is", yearly
main()
