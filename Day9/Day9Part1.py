import math
visited = []

H = (0, 0)
T = (0, 0) 

def dist(H, T):
    return round(math.sqrt((H[0] - T[0])**2 + (H[1] - T[1])**2))

with open('Day9/Day9Input.txt') as file:
    for line in file:
        line = line.split()
        for i in range(int(line[1])):
            match (line[0]):
                case 'U':
                    H = (H[0], H[1]+1)
                    if dist(H, T) > 1:
                        T = (T[0], T[1]+1)
                        if T[0] != H[0]:
                            T = (H[0], T[1])
                case 'D':
                    H = (H[0], H[1]-1)
                    if dist(H, T) > 1:
                        T = (T[0], T[1]-1)
                        if T[0] != H[0]:
                            T = (H[0], T[1])
                case 'L':
                    H = (H[0]-1, H[1])
                    if dist(H, T) > 1:
                        T = (T[0] - 1, T[1])
                        if T[1] != H[1]:
                            T = (T[0], H[1])
                case 'R':
                    H = (H[0]+1, H[1])
                    if dist(H, T) > 1:
                        T = (T[0] + 1, T[1])
                        if T[1] != H[1]:
                            T = (T[0], H[1])
            visited.append(T)
print(len(set(visited)))
