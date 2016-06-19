import car1

def main():
    year = raw_input("Enter the year model: ")
    make = raw_input("Enter the company who made the car: ")

    car = car1.Car(year,make)

    speed = int(raw_input("Enter the speed: "))

    for i in range(5):
        car.accelerateSpeed(speed)
        print 'Year:', car.get_year_model(),'\n', 'Make:', car.get_make()
        print 'Your speed now is:', speed
        speed = car.get_speed()

    speed = int(raw_input("Enter the speed: "))
    for i in range(5):
        car.breakSpeed(speed)
        print 'Year:', car.get_year_model(),'\n', 'Make:', car.get_make()
        print 'Your speed now is:', speed
        speed = car.get_speed()

main()
