def main():
    days = int(raw_input("How many days do you have sales for? "))

    sales = []

    for i in range(days):
        sale = int(raw_input("Enter the amount of say for days #" + str(i+1) + ' '))
        sales.append(sale)
    total = 0
    for i in sales:
        total += i
    print
    print "The total sales is",total

main()