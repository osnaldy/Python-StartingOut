def main():
    mass = int(raw_input("Enter the object's mass: "))
    weigth(mass)

def weigth(mass):
    weight = mass * 9.8
    if weight > 1000:
        print "You are too heavy"
    else:
        print "you are too light"
main()