file = open('Day1Input.txt')

totCalList = []

calories = 0

for line in file:
    if not line == '\n':
        calories += int(line)
    else:
        totCalList.append(calories)
        calories = 0

file.close()
totCalList.sort(reverse=True)
print(sum(totCalList[0:3]))