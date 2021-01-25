from math import *

f = open("3.txt", "r")

counter = 0
counter2 = 0
for i in f:
    if counter <= 30:
        if i[counter] == "#":
            print("bum")
            print(i)
            counter2 += 1
    else:
        counter -= 31
        counter = abs(counter)
        if i[counter] == "#":
            print("bum")
            print(i)
            counter2 += 1
    counter += 3

print(counter2)
