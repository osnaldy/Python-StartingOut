def main():
    number = raw_input("Enter a sequence of digits to be added: ")
    count = 0
    for i in number:
        num = int(i)
        count +=num
    print "The Sum of the Numbers you enter is:",count
main()