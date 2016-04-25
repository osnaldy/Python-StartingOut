from __future__ import print_function

for col in range(8):
    for row in range(col):
        for left in range(col - row):
            print (' ', end='')
        print('#')
