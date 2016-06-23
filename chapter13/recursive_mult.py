def main():

    recursive_multiplication(7, 4)

def recursive_multiplication(x, y):
    if x > 0:
        recursive_multiplication(x -1, y)
        print y
main()