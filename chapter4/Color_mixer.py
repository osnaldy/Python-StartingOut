def main():
    color = raw_input("Enter the first color: ")
    color2 = raw_input("Enter the second color: ")

    if (color  == 'red' and color2 == 'blue') or (color  == 'blue' and color2 == 'red'):
        print "Purple"
    elif (color  == 'red' and color2 == 'yellow') or (color  == 'yellow' and color2 == 'red'):
        print "Orange"
    elif (color  == 'blue' and color2 == 'yellow') or (color  == 'yellow' and color2 == 'blue'):
        print "Green"
    else:
        print "Error Message"
main()