with open('../inputs/day6.txt') as f:
    input = []
    for day in f.readline().rstrip().split(","):
        input.append(day)


def main():
    dict = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0
    }

    for val in input:
        dict[val] += 1

    day = 0
    while day < 256:
        numToAdd = dict['0']
        dict['0'] = dict['1']
        dict['1'] = dict['2']
        dict['2'] = dict['3']
        dict['3'] = dict['4']
        dict['4'] = dict['5']
        dict['5'] = dict['6']
        dict['6'] = dict['7']
        dict['6'] += numToAdd
        dict['7'] = dict['8']
        dict['8'] = numToAdd
        day += 1

    total = 0
    for x in dict:
        total += dict[x]

    print(f'Answer: {total}')

main()





