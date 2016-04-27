def main():
    name = open('record.txt', 'r')

    line = name.readline()
    count = 0
    while line != '':
        count += 1
        line1 = line.rstrip('\n')
        line = name.readline()
    print count, "Names were found in the file"
    name.close()

main()