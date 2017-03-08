import random

__author__ = 'trunghieu11'


def solve(n, totalBoxes, cowbells):
    cowbells = sorted(cowbells)
    left = 0
    right = n - 1
    answer = 0
    while right >= 0 and (right - left + 1) < totalBoxes * 2:
        answer = max(answer, cowbells[right])
        right -= 1
        totalBoxes -= 1
    while left < right:
        answer = max(answer, cowbells[left] + cowbells[right])
        left += 1
        right -= 1
    return answer


if __name__ == '__main__':
    n, totalBoxes = map(int, raw_input().split(" "))
    cowbells = map(int, raw_input().split(" "))

    # for test in range(10):
    #     n = random.randint(1, 10)
    #     totalBoxes = random.randint(1, 20)
    #     while n * 2 > totalBoxes:
    #         n = random.randint(1, 10)
    #         totalBoxes = random.randint(1, 20)
    #     cowbells = []
    #     for i in range(n):
    #         cowbells.append(random.randint(1, 10) + 1)
    #     print n, totalBoxes
    #     print cowbells

    print solve(n, totalBoxes, cowbells)