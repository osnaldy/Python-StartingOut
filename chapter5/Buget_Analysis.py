buget = int(raw_input("Enter the amount budgeted for the month: "))

total = 0

for i in range(6):
    expense = int(raw_input("Enter the total for each expense: "))
    total += expense

if total > buget:
    t1 = total - buget
    print "Your are over with", t1, 'Dollars'
else:
    t1 = buget - total
    print "Your budget is under with ", t1, 'Dollars'