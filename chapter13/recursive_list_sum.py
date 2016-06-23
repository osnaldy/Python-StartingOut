def main():
    numbers = eval(raw_input("Enter a list of numbers: "))
    print "The sum of the list of the list of numbers is:", list_sum(numbers)

def list_sum(list):

    if len(list) == 1:
        return list[0]

    return  list[0] + list_sum(list[1:])
main()