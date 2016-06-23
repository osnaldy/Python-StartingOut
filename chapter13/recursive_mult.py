def main():

    print recursive_multiplication(7, 4)

def recursive_multiplication(x, y):

   if x == 0:
       return 0
   elif x > 0:
       return y + recursive_multiplication(x -1, y)

main()