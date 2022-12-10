file = open('Day10/Day10Input.txt')

vals = []
crt = ['#']
current = 1

def strength(cyc):
    global vals
    return vals[cyc-2] * cyc

for line in file:
    if line.startswith('noop'):
        vals.append(current)
    elif line.startswith('addx'):
        vals.append(current)
        current = current + int(line.split()[1])
        vals.append(current)

for val in vals:
    if len(crt)%40 in range(val-1, val+2):
        crt.append('#')
    else:
        crt.append('.')

for i in range(0, 240, 40):
    temp = ''
    for j in range(i, i+40):
        temp += crt[j] + ' '
    print(temp)
