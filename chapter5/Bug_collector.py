days_attend = int(raw_input("Enter the amount of days attended: "))
total = 0
for sums in range(days_attend):
    amount = int(raw_input("Enter the collection per day: "))
    total += amount
print "The total collected by the Bug Collector:", total