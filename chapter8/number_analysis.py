def main():
    arr = []
    for i in range(20):
        num = float(raw_input("Enter number " + str(i + 1) + ' '))
        arr.append(num)

    minimum = min(arr)
    maximum = max(arr)
    print "The Minimum value is", minimum
    print "The Maximum value is", maximum

    total = 0
    for i in arr:
        total += i
    print "The total Sum is:", total
    average = total/len(arr)
    print "The Average is:", average

main()