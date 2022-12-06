file = open('Day4/Day4Input.txt')

total = 0
for line in file:
    left = line.split(",")[0].split("-")
    right = line.split(",")[1].split("-")
    
    if(int(right[0]) < int(left[0])):
        low = right
        high = left
    else:
        low = left
        high = right
    if (int(low[1]) >= int(high[0])):
        total += 1
print(total)
