def main():
    statetax()

def statetax():
    purchase = float(raw_input("Enter the amount purchased: "))
    state_tax = purchase * 0.02
    country_tax = purchase * 0.04
    total_purchase = (purchase+state_tax+country_tax)
    total_tax = country_tax + state_tax
    print "The amount is", purchase
    print "The state tax is", state_tax
    print "The country tax is", country_tax
    print "The total of the sale is", format(total_purchase, '.2f')
main()