import re


stacks = []
moverSize = 1

with open('Day5/Day5Input.txt') as reader:
    temp = ""
    while not temp == '\n':
        temp = reader.readline()
        stacks.append(temp)
    stacks.pop()
    stacks = [[row[i] for row in stacks] for i in range(len(stacks[0]))]
    for row in stacks:
        while(' ' in row):
            row.remove(' ')
    stacks = [list[-2::-1] for list in stacks if list != [] and list[0] not in ('[', ']', '\n')]
    

    temp = reader.readline()
    while not temp == '':
        nums = re.findall(r'\d+', temp)
        amount = int(nums[0])
        vFrom = int(nums[1]) - 1
        vTo = int(nums[2]) - 1
        temp = stacks[vFrom][len(stacks[vFrom]) - amount:]
        stacks[vFrom] = stacks[vFrom][:len(stacks[vFrom]) - amount:]
        stacks[vTo] += temp
        temp = reader.readline()
for item in stacks:
    print(item[-1])
