from __future__ import print_function
def main():
    sentence = "I SLEPT MOST OF THE NIGHT"
    new_for = sentence.split()
    print (sentence)
    for i in new_for:
        j = i[1:]
        latin = j+ i[0]+ 'AY'
        print (latin, end = " ")
main()