#This program reads through a paragraph and count the word's frequencies and
#returns it as a dictionary. words represents the key, and the number it appears
#represents the value
f = open('unique.txt','r').read().split()
dictionary = {}
for i in f:
    if not i in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
print dictionary
for k,v in dictionary.items():
    print k,v