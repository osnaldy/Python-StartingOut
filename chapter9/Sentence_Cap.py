from __future__ import print_function
def main():
    string = raw_input("Enter the string: ")
    cap_sentence(string)

def cap_sentence(s):
    new = s.split()
    for i in new:
        if i.startswith(i.lower()) and i.endswith('.') or i.startswith('m'):
            new = (i[0].upper() + i[1:])
        else:
            new = i
        print (new, end = " ")
main()