def main():

    num = int(raw_input("Enter a number: "))
    rec_print(num)

def rec_print(n):

    if n > 0:
        rec_print(n - 1)
        print n

main()