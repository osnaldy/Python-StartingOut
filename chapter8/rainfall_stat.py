#Design a program that lets the user enter the total rainfall
# for each of 12 months into a list.
#The program should calculate and display the total rainfall for the year,
# the average monthly
#rainfall, and the months with the highest and lowest amounts.

MONTHS = 12
def main():

    lists = get_rain_list()
    total = get_total(lists)
    minimum = min(lists)
    maximum = max(lists)

    print "The whole list entered is:", lists
    print "The total of the rain fall is:", total
    print "The minimum value is:", minimum
    print "The maximun value is", maximum
    monthly_average(lists)

def monthly_average(value):
    index = 0
    whole_total = 0
    for i in value:
        index +=1
        total = float(i) / MONTHS
        whole_total += total
        print "The Average for month #",index, "is", format(total, '.2f')
    print whole_total

def get_total(values):
    total = 0
    for i in values:
        total += i
    return total

def get_rain_list():
    total_rain = []
    for i in range(MONTHS):
        total_rainfall = int(raw_input("Enter the total rain for months #:" + str(i + 1) + ' '))
        total_rain.append(total_rainfall)
    return total_rain

main()