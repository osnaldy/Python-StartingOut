shares = 1000
price_per_share = 32.87
total = shares * price_per_share
joe_paid = total * 0.02
sold_share = 33.92
total2 = shares * sold_share
broker_earned = total2 * 0.02
total_left = total2 - broker_earned
print "Amount Joe paid", total
print "Amount Joe paid broker when he bought", joe_paid
print "Amount Joed sold the stock for", total2
print "Amount Joed paid broker when he sold", broker_earned
print "Amount left", total_left