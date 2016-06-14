import cellphone

def main():
    phone = make_list()

    print "Here is the data you have entered"
    display(phone)

def make_list():
    phone_list = []

    print "Enter data for five phones"
    for count in range(1,6):
        man = raw_input("Enter the manufacturer: ")
        mod = raw_input("Enter the model number: ")
        retail = float(raw_input("Enter the retail price: "))
        print

        phone = cellphone.Cellphone(man, mod, retail)

        phone_list.append(phone)
    return phone_list

def display(phone_list):
    for items in phone_list:
        print items.get_manufact()
        print items.get_model()
        print items.get_retail_price()
        print
main()