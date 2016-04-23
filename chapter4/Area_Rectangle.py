length = float(raw_input("Enter the length of rectangle: "))
width = float(raw_input("Enter the width of rectangle: "))
area = length*width

length2 = float(raw_input("Enter the length of rectangle: "))
width2 = float(raw_input("Enter the width of rectangle: "))
area2 = length2*width2

if area > area2:
    print "First rectangle is bigger"
elif area2 > area:
    print "Second rectangle is bigger"
else:
    print "The are the same size"