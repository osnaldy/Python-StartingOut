def main():
    scores = test_score()
    total = get_total(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores)-1)
    print "The Average with the lowest score dropped is:", format(average, '.2f')

def get_total(list_value):
    total = 0
    for i in list_value:
        total += i
    return total

def test_score():
    tests = []
    var = 'y'
    while var == 'y':
        score = float(raw_input("Enter the test score: "))
        tests.append(score)
        var = raw_input("y to continue, anything = no ")
        print
    return tests
main()