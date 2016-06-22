import vehicles
def main():

    used_car = vehicles.Car('Audi', 2007, 12500, 21500.00, 4)

    print 'Make:', used_car.get_make()
    print 'Model:', used_car.get_model()
    print 'Mileage:', used_car.get_mileage()
    print 'Price:', used_car.get_price()
    print 'Number of doors:', used_car.get_doors()

main()