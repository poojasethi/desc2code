import string

__author__ = 'trunghieu11'


def getDiff(a, b):
    for c in string.ascii_lowercase:
        if c != a and c != b:
            return c
    return a


def solve(n, k, a, b):
    totalA = k
    totalB = k
    diff = sum(a[i] != b[i] for i in range(n))
    answer = []
    for i in range(n):
        if a[i] != b[i]:
            if totalA == totalB == 0:
                return -1
            if totalA == totalB:
                if totalA + totalB > diff:
                    totalA -= 1
                    totalB -= 1
                    answer.append(getDiff(a[i], b[i]))
                else:
                    totalA -= 1
                    answer.append(b[i])
            else:
                if totalA > totalB:
                    totalA -= 1
                    answer.append(b[i])
                else:
                    totalB -= 1
                    answer.append(a[i])
            diff -= 1
        else:
            answer.append(a[i])
    if totalA + totalB > 0:
        if totalA == totalB:
            for i in range(n):
                if a[i] == b[i] and totalA > 0:
                    answer[i] = getDiff(a[i], b[i])
                    totalA -= 1
        else:
            return -1
    return ''.join(str(x) for x in answer)

if __name__ == '__main__':
    n, k = map(int, raw_input().split(" "))
    a = raw_input()
    b = raw_input()
    print solve(n, k, a, b)