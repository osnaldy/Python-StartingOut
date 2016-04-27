Num_days = 5
def main():
    sales = [0] * Num_days
    index = 0

    print "Enter the sales for each days"
    while index < Num_days:
        print 'Days #',index + 1,':'
        sales[index] = float(raw_input())
        index += 1
    print
    print "Here are the values that you have entered"
    for i in sales:
        print i

main()