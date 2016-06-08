def main():

    with open("unique.txt") as f:
        unique = []
        new = f.readline()
        while new != '':
            new = f.readline()
            for i in new.split():
                if not i in unique:
                    unique.append(i)
                    line = set(unique)
                else:
                    pass
        print line


main()
