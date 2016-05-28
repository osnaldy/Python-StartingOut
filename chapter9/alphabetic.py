from __future__ import print_function
def main():
    string = raw_input("Enter the number: ").upper()

    for char in range(len(string)):
        if string[char].isalpha():
            num = check_char(string[char])
        else:
            num = string[char]
        print(num, end = "")

def check_char(letter):
    if letter == 'A' or letter == 'B' or letter == 'C':
        return 2
    if letter == 'D' or letter == 'E' or letter == 'F':
        return 3
    if letter == 'G' or letter == 'H' or letter == 'I':
        return 4
    if letter == 'J' or letter == 'K' or letter == 'L':
        return 5
    if letter == 'M' or letter == 'N' or letter == 'O':
        return 6
    if letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S':
        return 7
    if letter == 'T' or letter == 'U' or letter == 'V':
        return 8
    if letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
        return 9
main()