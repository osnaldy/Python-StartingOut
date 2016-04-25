def main():
    print "Enter a number and start adding, or enter -1 to end the loop"
    print
    number = int(raw_input("Enter a number "))
    count = 0
    while number >0:
        count+=number
        number = int(raw_input("Enter a number "))
    print 'The Sum of all numbers entered is:',count
main()