def main():
    file_name = open('sales.txt')

    total = 0
    for sales in file_name:
        amount = float(sales)
        total += amount
        print amount
    print "Total Sum is:", total
main()