def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    my_sum = sums_range(numbers, 2, 6)

    print "The sum of numbers from 2 to 6 is:", my_sum

def sums_range(num_list, start, end):

    if start > end:
        return 0

    return num_list[start] + sums_range(num_list, start + 1, end)
main()