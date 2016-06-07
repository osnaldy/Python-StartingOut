# file_name = open('encryp.txt', 'wb')
# codes = {'A' : '!', 'a' : '1', 'B' : '2', 'b' : '@', 'C': '#', 'c' : '3',
#          'D' : '4', 'd' : '$', 'E' : '%', 'e' : '5', 'F' : '6', 'f' : '^',
#          'G' : '7', 'g' : '&', 'H' : '*', 'h' : '8', 'I' : '(', 'i' : '9',
#          'J' : ')', 'j' : '0', 'K' : '-', 'k' : '_', 'L' : '=', 'l' : '+',
#          'M' : '[', 'm' : '{', 'N' : ']', 'n' : '}', 'O' : '|', 'o' : ';',
#          'P' : ':', 'p' : ',', 'Q' : '<', 'q' : '.', 'R' : '>', 'r' : '/',
#          'S' : '!@', 's' : '#@', 'T' : '$#', 't' : '^%', 'U' : '&@', 'u' : '*!',
#          'V' : '@*', 'v' : ')!', 'W' : '#*', 'w' : '<#', 'X' : '^>', 'x' : '?(',
#          'Y' : '<!', 'y' : '?$', 'Z' : '/;', 'z' : ';:'
#          }
#
# for k, v in codes.items():
#     file_name.write(str(k) + ' ' + str(v)+'\n')
# file_name.close()
dice = []
with open('encryp.txt','r') as name:
    c = name.readline()
    while c != '':
        a = c.rstrip('\n').split()
        dice.append(a)
        c = name.readline()
    name.close()
with open('encryp2.txt', 'w') as p:
    for k, v in dice:
        writer = p.write(v[0:]+ '\n')
        print v[0:]

