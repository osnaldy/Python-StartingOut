def main():
    pennies = float(raw_input("Enter the numer of pennies: "))
    nickels = float(raw_input("Enter the numer of nickels: "))
    dimes = float(raw_input("Enter the numer of dimes: "))
    quaters = float(raw_input("Enter the numer of quaters: "))

    values_p = 0.01 * pennies
    values_n = 0.05 * nickels
    values_d = 0.10 * dimes
    values_q = 0.25 * quaters

    total = values_p + values_n + values_d + values_q

    if total == 1:
        print "you have a dollar"
    elif total < 1:
        print "Amount enter is less than a dollar"
    else:
        print 
main()