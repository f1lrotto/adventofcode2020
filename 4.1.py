'''
byr(Birth Year) - four digits; at least 1920 and at most 2002.
iyr(Issue Year) - four digits; at least 2010 and at most 2020.
eyr(Expiration Year) - four digits; at least 2020 and at most 2030.
hgt(Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid(Passport ID) - a nine-digit number, including leading zeroes.
'''

documents = open("4.txt", "r")
eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
people = [[]]  # list udajov individualnych ludi
count = 0

for line in documents:  # nacitat 1 cloveka do 1 listu v people
    if line is '\n':
        people.append([])
        count += 1
    else:
        line = line.strip('\n')
        line = line.split(' ')
        people[count].extend(line)

templist = []
for person in people:  # vymazat prazdne listy
    person.sort()
    if len(person) == 0:
        people.remove(person)

for person in people:  # odstrani cid kedze na nom nezalezi
    if "cid" in person[1] or "cid" in person[0]:
        person.remove(person[1])
    else:
        pass

for person in people:  # odstrani ppl co nemaju vsetky odaje
    if len(person) == 7:
        pass
    else:
        person.clear()
templist = []
for person in people:  # vymazat prazdne listy
    if len(person) == 7:
        templist.append(person)
people = templist

for person in people:  # xdxd
    person[0] = person[0].split(":")
    person[0][1] = int(person[0][1])

    person[1] = person[1].split(":")

    person[2] = person[2].split(":")
    person[2][1] = int(person[2][1])

    person[3] = person[3].split(":")

    person[4] = person[4].split(":")

    person[5] = person[5].split(":")
    person[5][1] = int(person[5][1])

    person[6] = person[6].split(":")

templist = []
for person in people:  # filter parametrov vek
    if person[0][1] in range(1920, 2003):
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov oci
    if person[1][1] in eye_color:
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov issue year
    if person[5][1] in range(2010, 2021):
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov issue ID
    if len(person[6][1]) == 9:
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov vlasy
    if '#' in person[3][1]:
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov vek
    if person[2][1] in range(2020, 2031):
        templist.append(person)
people = templist

templist = []
for person in people:  # filter parametrov vyska
    if len(person[4][1]) == 5:
        if 'cm' in person[4][1]:
            person[4][1] = person[4][1][:3]
            person[4][1] = int(person[4][1])
            if person[4][1] in range(150, 194):
                templist.append(person)
            person[4][1] = str(person[4][1])
for person in people:  # filter parametrov vyska
    if len(person[4][1]) == 4:
        if 'in' in person[4][1]:
            person[4][1] = person[4][1][:2]
            person[4][1] = int(person[4][1])
            if person[4][1] in range(59, 77):
                templist.append(person)

people = templist

print(len(people))
