file = open('Day3/Day3Input.txt')

dupes = []

def helper(first, second, third):
    for item in first:
        for item2 in second:
            for item3 in third:
                if item == item2 and item == item3:
                    return item
    print('ERROR')

while True:
    first = file.readline()
    second = file.readline()
    third = file.readline()

    if first == "":
        break
    dupes.append(helper(first, second, third))



total = 0
for item in dupes:
    if ord(item) >= 97:
        total += ord(item) - 96
    else:
        total += ord(item) - 38
print(total)