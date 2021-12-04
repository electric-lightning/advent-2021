with open('../inputs/day3.txt') as f:
    numbers = [line.rstrip() for line in f]

def resetGamma():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


gammaVals = resetGamma()


# for all lines, count the ones in each position
def countOnes(numbersin):
    for number in numbersin:
        for n in range(0, len(gammaVals)):
            if number[n] == '1':
                gammaVals[n] += 1


# get a binary string for most common values
def getBinaryOfMostCommonVals(totalNumbers):
    binary = ''
    for numOfOnes in gammaVals:
        numOfZeros = totalNumbers - numOfOnes
        if numOfOnes >= numOfZeros:
            binary += '1'
        else:
            binary += '0'

    return binary


index = 0


# Build a list with most common values
def getO2Numbers(numbersin, gammarate):
    new_list = []
    for num in numbersin:
        if num[index] == gammarate[index]:
            new_list.append(num)

    if getListLength(new_list) == 1:
        return new_list[0]

    return new_list


# Build a list with least common values
def getCO2Numbers(numbersin, gammarate):
    new_list = []
    for num in numbersin:
        if num[index] != gammarate[index]:
            new_list.append(num)

    if getListLength(new_list) == 1:
        return new_list[0]

    return new_list


def getListLength(data):
    return len(data) if isinstance(data, list) else 1


index = 0
filteredNumbers = numbers
for val in gammaVals:
    gammaVals = resetGamma()
    countOnes(filteredNumbers)
    binary = getBinaryOfMostCommonVals(len(filteredNumbers))
    filteredNumbers = getO2Numbers(filteredNumbers, binary)
    index += 1
    if getListLength(filteredNumbers) == 1:
        break

o2Rate = int(filteredNumbers, 2)


index = 0
filteredNumbers = numbers
for val in gammaVals:
    gammaVals = resetGamma()
    countOnes(filteredNumbers)
    binary = getBinaryOfMostCommonVals(len(filteredNumbers))
    filteredNumbers = getCO2Numbers(filteredNumbers, binary)
    index += 1
    if getListLength(filteredNumbers) == 1:
        break

co2Rate = int(filteredNumbers, 2)

print(f'o2Rate {o2Rate} co2Rate {co2Rate} = {o2Rate * co2Rate}')


