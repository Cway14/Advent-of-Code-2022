# same num of items in each compartment
# Lowercase item types a through z have priorities 1 through 26
# Uppercase item types A through Z have priorities 27 through 52 

f = open("input.txt", "r")
lines = f.readlines()
sum = 0

def convert_to_score(char):
    num = ord(char)
    if num >= 97 and num <= 122:
        return num - 96
    elif num >= 65 and num <= 90:
        return num - 38
    return num


# for each line, split into compartments
for line in lines:
    half = len(line) // 2
    c1 = line[0:half]
    c2 = line[half:]
    # for each letter in first compartment, check if it's in second
    for i in range(len(c1)):
        if c1[i] in c2:
            sum += convert_to_score(c1[i])
            break

print(sum)


f.close()
