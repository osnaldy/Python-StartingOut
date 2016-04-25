def main():
    days = int(raw_input("Enter the number of days: "))
    while days < 1:
        print "Days must be greater than 1"
        days = int(raw_input("Enter the number of days: "))
    penny = 0.5
    count = 0
    print 'Day\t  Pay'
    print '-------------'
    for i in range(1, days):
        count +=1
        penny *= 2
        print count, '\t ', penny
    total = penny/100
    print
    print "The Total in Dollars is $", format(total, '.2f')
main()