year_num = int(raw_input("Enter the number of years: "))

for year in range(year_num):
    total = 0.0
    for month in range(12):
        rain = int(raw_input("Enter the inches of rain for that month: "))
        total += rain
        month+=1
    average = float(total/month)
    print "Months\tTotal\tAverage"
    print "----------------------------"
    print month, '\t   ', total, '\t', format(average, '.2f')
    print