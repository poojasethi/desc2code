import random

__author__ = 'trunghieu11'


def solve(n, A):
    index = [-1 for i in range(n + 1)]
    index[0] = 0
    total = [0 for i in range(n + 1)]
    for x in A:
        if index[x - 1] >= 0:
            total[x] = total[x - 1] + 1
        else:
            total[x] = 1
        index[x] = 0
    return n - max(total)


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)

    # for i in range(10):
    #     n = random.randint(1, 10)
    #     A = [i + 1 for i in range(n)]
    #     random.shuffle(A)
    #
    #     print "------------------------"
    #     print n
    #     print A
    #     print solve(n, A)