#!/usr/bin/python
# A few Google interview questions

C1 = 100
L1 = [5,75,25]

C2 = 200
L2 = [150,24,79,50,88,345,3]

C3 = 8
L3 = [2,1,9,4,4,56,90,3]

def use_credit(credit, items):
    for i, x in enumerate(items):
        for z, y in enumerate(items):
            if z != i:
                if x + y == credit:
                    return [i+1,z+1]

print use_credit(C1, L1)
print use_credit(C2, L2)
print use_credit(C3, L3)

T1 = "this is a test"
T2 = "foobar"
T3 = "all your base"

def reverse_words(phrase):
    words = phrase.split(' ')
    words.reverse()
    return ' '.join(words)

print reverse_words(T1)
print reverse_words(T2)
print reverse_words(T3)

def get_phone_input(dial):
    mappings = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}
    keyindex = {' ': '0'}

    for x in mappings.keys():
        for y in range(len(mappings[x])):
            keyindex[mappings[x][y].lower()] = str(x)*(y+1)
    entry_code = ' '
    for x in dial:
        if entry_code[len(entry_code)-1] == keyindex[x][0] and keyindex[x][0] != '0':
            entry_code += ' '
        entry_code += keyindex[x]
    return entry_code[1:]

I1 = "hi"
O1 = "44 444"

I2 = "yes"
O2 = "999337777"

I3 = "foo  bar"
O3 = "333666 6660022 2777"

I4 = "hello world"
O4 = "4433555 555666096667775553"

print get_phone_input(I1)
print get_phone_input(I2)
print get_phone_input(I3)
print get_phone_input(I4)