f = open("1.txt", "r")

nums = []  # spracuje input z txt
right_nums = []
for line in f:
    nums.append(line)


def find(file):  # najde cisla suctu 2020
    for u in range(len(file)):  # zmaze \n z odpovede
        file[u] = int(file[u].strip())

    for i in range(len(file)):
        for k in range(len(file)):
            for m in range(len(file)):
                if int(file[i]) + int(file[k]) + int(file[m]) == 2020:
                    right_nums.append([file[i], file[k], file[m]])
    return right_nums


def ans(list):  # vypocita vysledok

    return list[0]*list[1]*list[2]


x = find(nums)
x = x[0]  # je tam duplikant


print(ans(x))
input()
