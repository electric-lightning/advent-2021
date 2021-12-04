with open('../inputs/day3.txt') as f:
    numbers = [line.rstrip() for line in f]

gammaVals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in numbers:
    for n in range(0, 12):
        if number[n] == '1':
            gammaVals[n] += 1

gammaRateBin = ''
epsilonRateBin = ''
for val in gammaVals:
    if val > len(numbers)-val:
        gammaRateBin += '1'
        epsilonRateBin += '0'
    else:
        gammaRateBin += '0'
        epsilonRateBin += '1'

gammaRate = int(gammaRateBin, 2)
epsilonRate = int(epsilonRateBin, 2)

print(f'Gamma: {gammaVals} gammaRate: {gammaRateBin} ({gammaRate}) epsilonRate: {epsilonRateBin} ({epsilonRate})')
print(f'Rate: {gammaRate*epsilonRate}')
