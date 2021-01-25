f = open("2.txt", "r")
counter = 0
counter2 = 0
final_count = 0
temp_list1 = []
temp_list2 = []
temp_list3 = []
slabikar = []


def split(word):
    return [char for char in word]


def edit(subor):
    global counter
    for i in subor:  # napasovat inpu do listu
        temp_list1.append(i)
    for i in temp_list1:  # odstranit n/ z listov
        temp_list2.append(i.strip())
    for i in temp_list2:  # rozdelit subor na 3 casti
        temp_list3.append(i.split())
    for i in temp_list3:  # rozdeli pocet pismen na zaciatku a konvertuje na int
        temp_list3[counter][0] = i[0].split("-")
        temp_list3[counter][0][0] = int(temp_list3[counter][0][0])
        temp_list3[counter][0][1] = int(temp_list3[counter][0][1])
        temp_list3[counter][1] = temp_list3[counter][1].strip()
        counter += 1
    for i in temp_list3:
        i[1] = i[1].replace(':', '')
    return(temp_list3)


def make(file):
    global final_count
    for i in file:  # najde ci je v hesle pozadovane pismeno
        countchar = 0
        x = False
        for u in i[2]:
            if u == i[1]:
                x = True
        if x:
            i.append(True)
        else:
            i.append(False)
        i.append(countchar)
    for i in file:
        a = i[0][0]
        b = i[0][1]
        if (i[2][a-1] == i[1]) ^ (i[2][b-1] == i[1]):
            i.append(1)
            final_count += 1
        else:
            i.append(0)
    return file


slabikar = edit(f)  # slabikar sa zformatuje
slabikar = make(slabikar)  # slabikar sa prepocita

print(final_count)
