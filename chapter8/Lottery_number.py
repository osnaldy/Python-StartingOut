import random

def main():

    lottery = []

    for i in range(7):
        number = random.randint(0,9)
        lottery.append(number)
    for i in lottery:
        print i
main()