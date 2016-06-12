class Customer():

    def __init__(self, name, balance = 0.00):
        self.name = name
        self.balance = balance
        print "Person's name:", self.name
        print "Person's balance:",self.balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise RuntimeError('Amount greater than the value balance')
        self.balance -= amount
        return  self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

def main():
    jeff = Customer('Osnaldy', 1000.00)
    print "Current Balance after withdraw is:", jeff.withdraw(400.00)

main()