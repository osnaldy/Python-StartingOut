def main ():
    feet = int(raw_input("Enter the number of feet to convert to inches: "))
    total = feet_to_inches(feet)
    if feet ==1:
        print feet, "foot equals", total, "inches"
    else:
        print feet, "feet equals", total, "inches"
def feet_to_inches(feet):
    inches = feet * 12
    return inches
main()