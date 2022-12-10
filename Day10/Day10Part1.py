file = open('Day10/Day10Input.txt')

vals = ['']
current = 1

def strength(cyc):
    global vals
    return vals[cyc-1] * cyc

for line in file:
    if line.startswith('noop'):
        vals.append(current)
    elif line.startswith('addx'):
        vals.append(current)
        current = current + int(line.split()[1])
        vals.append(current)
    
print(strength(20) +strength(60) + strength(100) + strength(140) + strength(180) + strength(220))

