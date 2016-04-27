def main():
    file_name = open('sales.txt')

    total = 0
    count = 0
    try:
        for sales in file_name:
            amount = float(sales)
            count += 1
            total += amount
            print amount
        average = total/count
        print "Total Sum is:", total
        print "Average is:", format(average, '.2f')
    except IOError as err:
        print err
    except ValueError as err:
        print err
main()