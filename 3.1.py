from math import *

slopes = [[1, 1], [3, 1], [5, 1], [7, 1]]
l = []

for u in range(4):
    index = 0
    pocetbuch = 0
    f = open("3.txt", "r")
    for riadok in f:
        if index <= 30:
            if riadok[index] == "#":
                pocetbuch += 1
        else:
            index -= 31
            index = abs(index)
            if riadok[index] == "#":
                pocetbuch += 1
        index += slopes[u][0]
    l.append(pocetbuch)
    f.close()

truefalse = True

f = open("3.txt", "r")
pocetbuch = 0
index = 0
for riadok in f:
    if truefalse:
        if index <= 30:
            if riadok[index] == "#":
                pocetbuch += 1
        else:
            index -= 31
            index = abs(index)
            if riadok[index] == "#":
                pocetbuch += 1
        index += 1
        truefalse = False
    else:
        truefalse = True
l.append(pocetbuch)

f.close()

print(l[0] * l[1] * l[2] * l[3] * l[4])
print(l)
