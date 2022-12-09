import math
visited = []

rope = [[0, 0] for i in range(10)]


def dist(H, T):
    return (H[0]-T[0], H[1]-T[1])


def adjust():
    global rope
    for i in range(len(rope)-1):
        d = dist(rope[i], rope[i+1])
        if abs(d[0]) > 1 or abs(d[1]) > 1:
            if d[0] > 0:
                rope[i+1][0] += 1
            elif d[0] < 0:
                rope[i+1][0] -= 1
            if d[1] > 0:
                rope[i+1][1] += 1
            elif d[1] < 0:
                rope[i+1][1] -= 1


with open('Day9/Day9Input.txt') as file:
    for line in file:
        line = line.split()
        for i in range(int(line[1])):
            match (line[0]):
                case 'U':
                    rope[0] = [rope[0][0], rope[0][1]+1]
                    adjust()
                case 'D':
                    rope[0] = [rope[0][0], rope[0][1]-1]
                    adjust()
                case 'L':
                    rope[0] = [rope[0][0]-1, rope[0][1]]
                    adjust()
                case 'R':
                    rope[0] = [rope[0][0]+1, rope[0][1]]
                    adjust()
            visited.append(list.copy(rope[-1]))
visited = [tuple(el) for el in visited]

print(len(set(visited)))
