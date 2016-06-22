def main():

    string = count_x('xykxkjxxhx')
    print string

def count_x(str_):

    if str_ == '':
        return 0

    last = str_[-1]

    if last == 'x':
        return count_x(str_[:-1]) + 1
    return count_x(str_[:-1]) + 0
main()