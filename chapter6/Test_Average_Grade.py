def main():
    count = 0
    for i in range(5):
        score = int(raw_input("Enter the test #" + str(i+1) + ': '))
        count += score
        print determine_grade(score)
    print calc_average(count)

def calc_average(num):
    avg = num / 5.0
    return avg

def determine_grade(test):
    if test >= 90 and test <= 100:
        return 'A'
    elif test >= 80 and test <= 89:
        return  'B'
    elif test >= 70 and test <= 79:
        return  'C'
    elif test >= 60 and test <= 69:
        return 'D'
    elif test < 60:
        return 'F'
main()