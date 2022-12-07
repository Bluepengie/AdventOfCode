import operator

file = open('Day7/Day7Input.txt')

currentDir = ""
lastDir = []
filesCounted = []
dirSizes = {'/': 0}

def cd(cmd):
    global currentDir
    global lastDir

    cmd = cmd[5:].strip(" \n")
    if cmd == "..":
        currentDir = currentDir[:len(currentDir) - len(lastDir.pop()) - 1]
    elif cmd != "/":
        currentDir = currentDir + cmd + "/"
        lastDir.append(cmd)

    else:
        lastDir = ["/"]
        currentDir = "/"

def ls(): 
    global currentLine
    global dirSizes
    global filesCounted
    global file
    currentLine = file.readline()[:-1]
    

    while currentLine != '' and currentLine[0] != "$":
        if currentLine[:3] == "dir":
            newDir = currentDir + currentLine[4:] + '/'
            if not newDir in dirSizes:
                dirSizes.update({newDir: 0})
        else:
            args = currentLine.split()
            if not args[1] in filesCounted:
                filesCounted.append(currentDir + args[1])
                dirsToAdd = currentDir
                idx = len(lastDir) - 1
                while dirsToAdd != '':
                    dirSizes.update({dirsToAdd: dirSizes[dirsToAdd] + int(args[0])})
                    dirsToAdd = dirsToAdd[:-len(lastDir[idx])-1]
                    idx -= 1
        currentLine = file.readline()[:-1]

currentLine = " "
while currentLine != '':
    if currentLine[2:4] == "cd":
        cd(currentLine)
        currentLine = file.readline()
    elif currentLine[2:4] == "ls":
        ls()
    else:
        currentLine = file.readline()

total = 70000000
used = dirSizes['/']

free = total - used
targetToDel = 30000000 - free
sorted = sorted(dirSizes.items(), key=lambda kv: kv[1])

for item in sorted:
    if item[1] >= targetToDel:
        print(item[1])
        exit()
