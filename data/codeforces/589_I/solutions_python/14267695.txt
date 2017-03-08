__author__ = 'trunghieu11'


def solve(ballCount, partCount, colors):
    each = ballCount / partCount
    total = {}
    for x in colors:
        total[x] = total[x] + 1 if x in total else 1
    answer = 0
    for x in total.keys():
        answer += max(0, total[x] - each)
    return answer


if __name__ == '__main__':
    ballCount, partCount = map(int, raw_input().split(" "))
    colors = map(int, raw_input().split())
    print solve(ballCount, partCount, colors)