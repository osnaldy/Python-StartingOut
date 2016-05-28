def main():
    files = open('num.txt', 'r')
    f = files.readlines()
    arr = []
    for i in f:
        new = float(len(i.rstrip('\n').split()))
        j = i.rstrip().split()
        arr.append(new)
        print new, j
    count = sum(arr)
    c = 0
    for i in range(len(arr)):
        avg = arr[i]/count
        c += 1
        print "The Average number of words for line #" + str(c)\
            + ' ' + format(avg, '.2f')
main()