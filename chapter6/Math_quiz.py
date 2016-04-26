import random

def main():
    total = int(raw_input("Enter the sum of both random numbers: "))
    number_sum = randomize()
    if total == number_sum:
        print "Congrats you guessed the sum of the numbers which is", number_sum
    else:
        print "Sorry!!! you could not guess the number"
        print "The sum is", number_sum
def randomize():
    random.seed(11)
    count = 0
    for i in range(2):
        number = random.randint(1,100)
        count += number
    return count
main()