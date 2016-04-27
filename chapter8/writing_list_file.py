def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas', 'San Antonio']

    out_file = open('cities.txt', 'w')

    for i in cities:
        out_file.write(i + '\n')
    out_file.close()
main()