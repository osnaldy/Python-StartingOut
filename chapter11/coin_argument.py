import coin_demo

def main():
    my_coin = coin_demo.Coin()
    print my_coin.get_sideup()

    flip(my_coin)

    print my_coin.get_sideup()

def flip(coin_obj):
    coin_obj.toss()
main()