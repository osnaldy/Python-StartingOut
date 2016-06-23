def main():

    recur_line(10)

def recur_line(n):

    if n > 0:
        recur_line(n - 1)
        print '*' * n
main()