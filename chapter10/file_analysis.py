with open('new.txt') as f, open('unique.txt') as k:
    j = set(f.read().split())
    i = set(k.read().split())
    t = j.symmetric_difference(i)
    print t
    x = j.intersection(i)
    print x
    v = j.difference(i)
    print v
    e = i.difference(j)
    print e