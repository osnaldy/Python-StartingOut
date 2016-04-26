def main():

    prime_number = 0
    for i in range(1, 101):
        if is_prime(i):
            prime_number += 1
            print i
    print "There are", prime_number, "Prime Numbers between 1 and 100"

def is_prime(n):

    if n >= 2:
        for i in range(2, n):
            if not (n % i):
                return ''
    else:
        return ''
    return 'A Prime'

main()


