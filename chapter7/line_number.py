from __future__ import print_function
def main():
    file_name = raw_input("Enter the file name: ")
    name = open(file_name, 'r')

    count = 0

    for line in name:
        count += 1
        expression = float(line)
        print (count,': ', expression, sep='')
main()