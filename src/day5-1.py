with open('../inputs/day5.txt') as f:
    input = [line.rstrip() for line in f]


class PointProcessor:
    __points = {}

    def addPoint(self, coordFrom, coordTo):
        fromXY = coordFrom.split(',')
        toXY = coordTo.split(',')

        if fromXY[0] == toXY[0]:
            x = int(fromXY[0])
            step = 1 if int(fromXY[1]) < int(toXY[1]) else -1
            for n in range(int(fromXY[1]), int(toXY[1])+step, step):
                key = f'{x},{n}'
                val = self.__points.get(key)
                if val:
                    val += 1
                    self.__points[key] = val
                else:
                    self.__points.setdefault(key, 1)
        elif fromXY[1] == toXY[1]:
            y = int(fromXY[1])
            step = 1 if int(fromXY[0]) < int(toXY[0]) else -1
            for n in range(int(fromXY[0]), int(toXY[0])+step, step):
                key = f'{n},{y}'
                val = self.__points.get(key)
                if val:
                    val += 1
                    self.__points[key] = val
                else:
                    self.__points.setdefault(key, 1)
        else:
            # part2
            fromX = int(fromXY[0])
            toX = int(toXY[0])
            fromY = int(fromXY[1])
            toY = int(toXY[1])

            stepX = 1 if fromX < toX else -1
            stepY = 1 if fromY < toY else -1
            doIt = True
            while doIt:
                key = f'{fromX},{fromY}'
                val = self.__points.get(key)
                if val:
                    val += 1
                    self.__points[key] = val
                else:
                    self.__points.setdefault(key, 1)

                if fromX == toX and fromY == toY:
                    doIt = False
                fromX += stepX
                fromY += stepY


    def getOverlappingPoints(self, overlappingVal):
        count = 0
        for val in self.__points.values():
            if val >= overlappingVal:
                count += 1
        return count


def main():
    more = True
    pp = PointProcessor()

    while more:
        try:
            coords = input.pop(0).split(' -> ')
            pp.addPoint(coords[0], coords[1])

        except IndexError:
            more = False

    print(f'Points that overlap more than 2x: {pp.getOverlappingPoints(2)}')

main()





