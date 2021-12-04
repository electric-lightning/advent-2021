with open('../inputs/day1.txt') as f:
    depths = [line.rstrip() for line in f]

increases = 0
offset = 0
lastDepth = -1
currentDepth = 0
try:
    for depth in depths:
        for val in range(offset, offset+3):
            currentDepth += int(depths[val])
        offset += 1

        if lastDepth != -1 and int(currentDepth) > int(lastDepth):
            increases = increases + 1
        lastDepth = currentDepth
        currentDepth = 0
except IndexError:
    print(f'Increases: {increases}')
