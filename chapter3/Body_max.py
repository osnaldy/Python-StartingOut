def main():

    print "First lets calculate your height into inches, a get that number"
    print "remember that one one foot equals to 12 inches"
    foot = int(raw_input("Please enter how many feet tall you are: "))
    inches  = foot * 12
    print "This is your height in foot converted to inches", inches
    mass_index()

def mass_index():
    weight = float(raw_input("Enter your weight: "))
    height = float(raw_input("Please enter your height in inches 1 foot is equals to 12 inches: "))
    BMI = (weight * 703)/height**2
    print "This is you BMI", format(BMI, '.2f')
main()