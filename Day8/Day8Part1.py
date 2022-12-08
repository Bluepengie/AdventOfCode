import numpy

forest = []
with open('Day8/Day8Input.txt') as file:
    temp = file.readline().strip()
    while temp != '':
        forest.append(temp)
        temp = file.readline().strip()

forest90 = [[row[i] for row in forest] for i in range(len(forest[0]))]

visible = [[[] for i in forest[0]] for j in forest]


for j in range(len(forest)):
    row = forest[j]
    for i in range(len(row)):
        lVis = 0
        for left in reversed(row[:i]):
            lVis += 1
            if left >= row[i]:
                break
        visible[j][i].append(lVis)

        rVis = 0
        for right in row[i+1:]:
            rVis += 1
            if right >= row[i]:
                break
        visible[j][i].append(rVis)

        
for j in range(len(forest90)):
    row = forest90[j]
    for i in range(len(row)):
        lVis = 0
        for left in reversed(row[:i]):
            lVis += 1
            if left >= row[i]:
                break
        visible[i][j].append(lVis)

        rVis = 0
        for right in row[i+1:]:
            rVis += 1
            if right >= row[i]:
                break
        visible[i][j].append(rVis)



maxScene = 0
for row in visible:
    for ele in row:
        ele = numpy.prod(ele)
        if ele > maxScene:
            maxScene = ele
print(maxScene)