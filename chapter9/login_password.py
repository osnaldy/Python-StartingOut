def main():

    password = raw_input("Enter the password: ")

    while not valid_password(password):
        print "That password is not valid"
        password = raw_input("Enter password again: ")
    print "That is a valid password!!", password

def valid_password(password):
    correct_length = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 7:
        correct_length = True

        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.islower():
                has_lower = True
            if ch.isdigit():
                has_digit = True

    if correct_length and has_upper and \
        has_lower and has_digit:
        is_valid = True
    else:
        is_valid = False

    return is_valid

main()