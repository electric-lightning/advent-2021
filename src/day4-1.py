import re

with open('../inputs/day4.txt') as f:
    input = [line.rstrip() for line in f]


class Board:
    __board = {}
    __lastNumber = 0

    def __init__(self, boardNumbers):
        self.__board = {}
        for num in boardNumbers:
            self.__board.setdefault(num, 0)

    def getLastNumber(self):
        return self.__lastNumber

    def addBall(self, number):
        self.__lastNumber = number
        if number in self.__board:
            self.__board[number] = 1


    def hasWinningLine(self):
        if self.__isWinningHorozontalLine():
            return True
        if self.__isWinningVerticalLine():
            return True
        return False


    def getSumOfUnmarkedNumbers(self):
        total = 0
        for tuple in self.__board.items():
            if tuple[1] == 0:
                total += int(tuple[0])
        return total


    def __isWinningHorozontalLine(self):
        offset = 0
        lineComplete = True
        values = list(self.__board.values())
        while offset + 5 <= len(self.__board):
            for n in range(offset, offset+5):
                if values[n] == 0:
                    lineComplete = False
                    break

            if lineComplete:
                return True

            lineComplete = True
            offset += 5

        return False


    def __isWinningVerticalLine(self):
        offset = 0
        col = 0
        lineComplete = True
        values = list(self.__board.values())
        v_numbers = []
        while col < 5:
            offset = 0
            while offset + 5 <= len(self.__board):
                v_numbers.append(values[col+offset])
                offset += 5

            for n in range(5):
                if v_numbers[n] == 0:
                    lineComplete = False
                    break

            if lineComplete:
                return True

            v_numbers.clear()
            lineComplete = True
            col += 1

        return False


def main():
    balls = input.pop(0).split(',')

    boards = []
    lines = []
    moreBoards = True
    while moreBoards:
        try:
            line = input.pop(0)
        except IndexError:
            line = []
            moreBoards = False

        if not line:
            if not lines:
                continue
            else:
                boards.append(Board(lines))
                lines = []
        else:
            lines += re.split('\\s+', line.strip())

    weHaveAWinner = False
    for nextBall in balls:
        for board in boards:
            board.addBall(nextBall)
            if board.hasWinningLine():
                print(f'Winning number {int(board.getLastNumber()) * int(board.getSumOfUnmarkedNumbers())} '
                      f'last ball {board.getLastNumber()} '
                      f'sum of unmarked numbers {board.getSumOfUnmarkedNumbers()}')
                weHaveAWinner = True
                break
        if weHaveAWinner:
            break


main()





