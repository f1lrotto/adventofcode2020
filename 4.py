documents = open("4.txt", "r")

list_of_docs = [[]]
count = 0

for line in documents:
    if line == "\n":
        list_of_docs.append([])
        count += 1

    else:
        line = line.strip()
        line = line.split("''")

        list_of_docs[count].append(line)

count = 0

x = []
for line in list_of_docs:
    x.append([])
    for length in range(len(line)):
        x[count] = x[count]+line[length]
        x[count]
    count += 1

for line in x:
    for index in range(len(line)):
        if "byr" in line[index]:
            line.append(True)
        if "iyr" in line[index]:
            line.append(True)
        if "eyr" in line[index]:
            line.append(True)
        if "hgt" in line[index]:
            line.append(True)
        if "hcl" in line[index]:
            line.append(True)
        if "ecl" in line[index]:
            line.append(True)
        if "pid" in line[index]:
            line.append(True)
count = 0

indexy = []
for line in x:
    if len(line) >= 7:
        if line[-7] == True:
            indexy.append(count)
    else:
        pass
    count += 1


print(len(indexy))
