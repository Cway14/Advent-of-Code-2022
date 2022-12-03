import part1

f = open("input.txt", "r")
lines = f.readlines()
sum = 0

# for every 3 lines, find the character that appears in all 3
for i in range(0, len(lines)-3, 3):
    print(i)
    c1 = lines[i]
    c2 = lines[i+1]
    c3 = lines[i+2]
    for j in range(len(c1)):
        if c1[j] in c2 and c1[j] in c3:
            sum += part1.convert_to_score(c1[j])
            break

print(sum)

