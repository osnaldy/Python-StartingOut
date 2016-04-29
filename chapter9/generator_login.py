def main():
    first = raw_input("Enter first name: ")
    last = raw_input("Enter last name: ")
    id_num = raw_input("Enter the Id Number: ")

    print "Your system login is"
    print get_login(first,last,id_num)

def get_login(first,last,id_num):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = id_num[-3:]
    login = set1 + set2 + set3
    return login
main()