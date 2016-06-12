import random

# The Coin class simulates a coin that can
# be flipped.
class Coin:

    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup
def main():
    my_coin = Coin()
    # Display the side of the coin that is facing up.
    print "This side is up: ", my_coin.get_sideup()

    # Toss the coin.
    print ("Im tossing the coin......")
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print "This side is up: ", my_coin.get_sideup()

main()