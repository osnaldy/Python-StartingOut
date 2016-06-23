def main():

    list = eval(raw_input("Enter a list of numbers: "))
    print "The largest number is :", largest(list)

def largest(list):
    if len(list) == 1:
        return list[0]

    large = largest(list[1:])

    if large > list[0]:
        return large
    return list[0]
main()