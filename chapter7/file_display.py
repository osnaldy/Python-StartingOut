def main():
    number = open('numbers.txt', 'r')

    line = number.readline()

    while line != '':
        amount = float(line)

        print format(amount, '.2f')

        line = number.readline()
    number.close()
main()