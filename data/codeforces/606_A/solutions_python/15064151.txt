__author__ = 'trunghieu11'


def solve(firstSphere, secondSphere):
    for i in range(3):
        minVal = min(firstSphere[i], secondSphere[i])
        firstSphere[i] -= minVal
        secondSphere[i] -= minVal
    return "Yes" if sum(x / 2 for x in firstSphere) >= sum(secondSphere) else "No"


if __name__ == '__main__':
    firstSphere = map(int, raw_input().split(" "))
    secondSphere = map(int, raw_input().split(" "))
    print solve(firstSphere, secondSphere)