def main():

    number = int(raw_input("Enter a number: "))
    fact = factorial(number)

    print "The factorial number of", number, 'is', fact

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
main()