def main():
    value = float(raw_input("Please enter the actual value: "))
    totals(value)

def totals(num):

    assessment = num * 0.60
    property_tax = assessment * 0.0064
    print "The actual value is:", num
    print "The assessment is:", assessment
    print "The property tax is:", property_tax
main()
