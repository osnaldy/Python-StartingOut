def main():
    #open the file
    file = open('cities.txt', 'r')
    #read the file
    cities = file.readlines()
    #close the file
    file.close()

    index = 0

    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print cities

main()