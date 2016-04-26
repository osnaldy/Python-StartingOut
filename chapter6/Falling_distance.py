GRAVITY = 9.8
def main():
    count = 0
    print "Time\tDistance"
    for i in range(1, 11):
        count +=1
        print i, '\t   ', fall_distance(i)

def fall_distance(time):
    d = 1/5.0 * GRAVITY * time**2
    return d
main()
