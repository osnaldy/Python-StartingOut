def main():
    num = int(raw_input("Enter the number to be converted to Roman Numeral: "))
    print converter(num)

def converter(num):
    if num == 1:
        return 'I'
    elif num == 5:
        return 'V'
    elif num == 10:
        return 'X'
    elif num == 50:
        return 'L'
    elif num == 100:
        return 'C'
    elif num == 500:
        return 'D'
    elif num == 1000:
        return 'M'
main()