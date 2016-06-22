def main():

    num_list = [1,2,3,4,5]

    my_mult = range_mult(num_list, 3, 4)

    print "The multiplication of numbers from index 3 to 4 is:", my_mult

def range_mult(num_list, start, end):

    if start > end:
        return 1

    return num_list[start] * range_mult(num_list, start + 1, end)

main()