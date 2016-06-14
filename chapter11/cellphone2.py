import cellphone

def main():
    man = raw_input("Enter the manufacturer: ")
    mod = raw_input("Enter the model number: ")
    retail = float(raw_input("Enter the retail price: "))

    phone = cellphone.Cellphone(man, mod, retail)

    print "Here is the Data that you have entered "
    print "Manufacturer:", phone.get_manufact()
    print "Model Number:", phone.get_model()
    print "Retail Price:", phone.get_retail_price()

main()