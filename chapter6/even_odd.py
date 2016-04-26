import random
def main():
    count_even = 0
    count_odd = 0
    for i in range(100):
        number =  random.randint(1,100)
        if number % 2 == 0:
            count_even +=1
            print count_even, 'Even'
        else:
            count_odd +=1
            print count_odd, 'Odd'

main()