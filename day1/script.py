
f = open("./calories.txt", "r")

topThree = [0, 0, 0]
currentCount = 0
for line in f:
    if line == '\n':
        if currentCount > topThree[0]:
            topThree[0] = currentCount
            topThree.sort()
        currentCount = 0
    else:
        currentCount += int(line)

print(topThree[0])
print(topThree[1])
print(topThree[2])
print(topThree[0] + topThree[1] + topThree[2])
