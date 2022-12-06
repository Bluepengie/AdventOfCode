file = open('Day6/Day6Input.txt')

packet = file.readline()

for i in range(len(packet)-14):
    temp = packet[i:i+14]
    if len(set(temp)) == 14:
        print(i+14)
        break
