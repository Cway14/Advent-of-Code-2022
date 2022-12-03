

f = open("calories.txt", "r")

max = 0
currentCount = 0
for line in f:
    if line == '\n':
        if currentCount > max:
            max = currentCount
        currentCount = 0
    else:
        currentCount += int(line)

print(max)
