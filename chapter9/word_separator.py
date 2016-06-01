def main():
    result = ""
    string = raw_input("Enter a Sentence without space: ")
    for i in string:
        if i.isupper():
            result += " "
            result += i.lower()
        else:
            result += i
    print result[1].upper() + result[2:]
main()