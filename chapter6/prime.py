def main():
    number = int(raw_input("Enter the number to check if it's prime: "))
    print 'Number', number, 'is', is_prime(number), 'Number'

def is_prime(n):
        if n < 2:
            return 'Not a Prime'
        if n == 2:
            return 'a Prime'
        else:
            for div in range(2, n):
                if n % div == 0:
                    return 'Not a Prime'
                return 'a Prime'
main()