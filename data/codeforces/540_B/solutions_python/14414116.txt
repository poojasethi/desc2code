__author__ = 'trunghieu11'


def solve(n, k, p, x, y, A):
    need = x - sum(A)
    remain = n - k
    if need < remain:
        return -1
    answer = []
    while need - y >= remain and remain > 0:
        answer.append(y)
        need -= y
        remain -= 1

    for i in range(remain):
        val = min(need - (remain - i - 1), p)
        need -= val
        answer.append(val)

    if need > 0:
        for i in range(len(answer)):
            val = min(p - answer[i], need)
            answer[i] += val
            need -= val

    A = A + answer
    A = sorted(A)
    return -1 if A[n / 2] < y else ' '.join(str(x) for x in answer)


if __name__ == '__main__':
    n, k, p, x, y = map(int, raw_input().split(" "))
    if k != 0:
        A = map(int, raw_input().split(" "))
    else:
        A = []
    print solve(n, k, p, x, y, A)