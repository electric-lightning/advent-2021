class Fish:
    def __init__(self, daysUntilspawn):
        self.__spawnCounter = int(daysUntilspawn)
        self.__timeToSpawn = False

    def newDay(self):
        if self.__spawnCounter == 0:
            self.__spawnCounter = 6
            self.__timeToSpawn = True
        else:
            self.__timeToSpawn = False
            self.__spawnCounter -= 1

    def timeToSpawn(self):
        return self.__timeToSpawn


with open('../inputs/day6.txt') as f:
    fish = []
    for day in f.readline().rstrip().split(","):
        fish.append(Fish(day))


def main():
    day = 0

    while day < 80:
        count = len(fish)

        for offset in range(0, count):
            fish[offset].newDay()
            if fish[offset].timeToSpawn():
                fish.append(Fish(8))

        day += 1

    print(f'Answer: {len(fish)}')

main()





