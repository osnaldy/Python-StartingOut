def main():
    number = int(raw_input("Enter for how many days you have sales: "))

    sales_file = open('sales.txt', 'w')

    for i in range(1, number+1):
        sales = int(raw_input("Enter the sales for day #" + str(i) + ':'))

        sales_file.write(str(sales)+'\n')

    sales_file.close()
    print "Data has been written to the file sales.txt"
main()
