def main():

    num1 = int(raw_input("Enter the first number: "))
    num2 = int(raw_input("Enter the second number: "))

    print gdc(num1, num2)

def gdc(x, y):

    if x % y == 0:
        return y

    return gdc(x, x % y)

main()