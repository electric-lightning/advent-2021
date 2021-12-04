with open('../inputs/day1.txt') as f:
    depths = [line.rstrip() for line in f]

increases = 0
lastDepth = -1
for depth in depths:
    if lastDepth != -1 and int(depth) > int(lastDepth):
        increases = increases + 1
    lastDepth = depth
print(f'Increases: {increases}')
