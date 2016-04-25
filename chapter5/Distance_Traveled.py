speed = int(raw_input("Enter the speed the of the vehicle in MPH: "))
hour = int(raw_input("Enter the amount of hours travelled: "))
print
distance = 0
count = 0
print "Hours\tDistance Travelled"
print "-------------------------"
for i in range(0, hour):
    i +=1
    distance = i * speed
    print i, '\t         ', distance

