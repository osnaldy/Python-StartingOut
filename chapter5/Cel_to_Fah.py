def main():

    start = int(raw_input("Enter the start point: "))
    end = int(raw_input("Enter the end point: "))
    print "Fahrenheit\tCelsius"
    fahrenheit(start, end)

def fahrenheit(x,b):
        c = -1
        for i in range(x, b+1):
            c+=1
            f = 9.0/5*i+32
            print c, '\t        ',round(f)
main()