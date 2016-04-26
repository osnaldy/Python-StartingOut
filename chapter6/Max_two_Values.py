def main():
    a = int(raw_input("Enter the value of a: "))
    b = int(raw_input("Enter the value of b: "))
    print "The greater value is", maximum(a, b)
def maximum (a, b):
    if a > b:
        return a
    else:
        return b

main()