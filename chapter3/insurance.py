def main():

    min_insurance()

def min_insurance():
    cost = float(raw_input("Enter the replacement cost: "))
    min = cost * 0.8
    print "The minimum amount of cost of insurance is", min
main()