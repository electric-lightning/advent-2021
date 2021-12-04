with open('../inputs/day2.txt') as f:
    instructions = [line.rstrip() for line in f]

distance = 0
depth = 0
aim = 0
for instr in instructions:
    data = instr.split()
    steer = data[0]
    val = int(data[1])
    if steer == 'forward':
        depth += val * aim
        distance += val
    elif steer == 'down':
        aim += val
    else:
        aim -= val

print(f'distance {distance} depth {depth} total {distance*depth}')
