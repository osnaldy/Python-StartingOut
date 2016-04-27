import random

ROW = 3
COL = 4

def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    #Fill the list with random numbers
    for r in range(ROW):
        for c in range(COL):
            values[r][c] = random.randint(1,100)

    print values
    print
    for r in range(ROW):
        for c in range(COL):
            print values[r][c]
    print
    names = ('Jose', 'Pedro', 'Carlos')
    for i in range(len(names)):
        print names[i]
main()
