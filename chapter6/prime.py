def main():
    number = int(raw_input("Enter the number to check if it's prime: "))
    print 'Number', number, 'is', is_prime(number), 'Number'

def is_prime(n):
    if n >=2:
        for i in range(2,n):
            if not (n % i):
                return 'Not a Prime'
    else:
        return 'Not a Prime'
    return 'a Prime'
main()