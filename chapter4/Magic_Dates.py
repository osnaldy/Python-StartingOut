def main():
    month = int(raw_input("Enter the month: "))
    day = int(raw_input("Enter the day: "))
    year = int(raw_input("Enter two digits for the year: "))

    value = month*day

    if value == year:
        print "this is magic"
    else:
        print "This is not magic"
main()