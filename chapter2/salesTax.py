purchase = float(raw_input("Enter the total purchase: "))
state_tax = 0.02
country_tax = 0.04
total = (purchase * state_tax) + (purchase * country_tax)
final_total = total + purchase
print "The amount is", purchase
print "The state tax is", purchase * state_tax
print "The country tax is", purchase * country_tax
print "The total of the sale is", format(final_total, '.2f')
