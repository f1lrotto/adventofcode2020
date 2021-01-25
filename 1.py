f = open("1.txt", "r")

nums = []  # spracuje input z txt
right_nums = []
for line in f:
    nums.append(line)


def find(file):  # najde cisla suctu 2020
    for i in range(len(file)):
        for k in range(len(file)):
            if int(file[i]) + int(file[k]) == 2020:
                right_nums.append([file[i], file[k]])
    return right_nums


def ans(list):  # vypocita vysledok
    for i in range(len(list)):  # zmaze \n z odpovede
        list[i] = int(list[i].strip())

    return list[0]*list[1]


x = find(nums)
x = x[0]  # je tam duplikant


print(ans(x))
input()
