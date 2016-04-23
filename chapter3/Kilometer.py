def main():
    convert()
def convert():
    kilo = float(raw_input("Enter the distance in kilometers and convert it to miles: "))
    miles = kilo * 0.6214
    print kilo, "in kilometers is equals to ", format(miles, '.2f'), "converted to miles",
main()