def main():

    num = int(raw_input("Enter a number: "))
    value = cut_number(num)
    print "The sum of each digits in that number is:", value

#sum of a digit of a number
def cut_number(num):

    if num == 0:
        return 0

    return cut_number(num / 10) + num % 10

main()