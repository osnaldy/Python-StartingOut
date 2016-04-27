def main():
    sales_file = open('sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)

        print format(amount, '.1f')

        line = sales_file.readline()
    sales_file.close()
main()