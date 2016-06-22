def main():

    print "The first 10 numbers \n of the Fibonacci series"

    for number in range(1,11):
        print fibo(number)

def fibo(num):

    if num == 0:
        return 0

    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

main()