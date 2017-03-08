__author__ = 'trunghieu11'


def solve(n, m, f, b):
    counter = {}
    for x in f:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1
    for x in b:
        if x not in counter:
            return "Impossible"
    for x in b:
        if counter[x] > 1:
            return "Ambiguity"
    idx = {}
    for i in range(n):
        idx[f[i]] = i

    answer = "Possible\n"
    answer += ' '.join(str(idx[x] + 1) for x in b)
    return answer



if __name__ == '__main__':
    n, m = map(int, raw_input().split(" "))
    f = map(int, raw_input().split(" "))
    b = map(int, raw_input().split(" "))
    print solve(n, m, f, b)