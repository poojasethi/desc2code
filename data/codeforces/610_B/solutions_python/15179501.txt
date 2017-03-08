__author__ = 'trunghieu11'


def solve(n, A):
    minVal = min(A)
    idx = [i for i in range(n) if A[i] == minVal]
    answer = 0
    for i in range(1, len(idx)):
        answer = max(answer, idx[i] - idx[i - 1] - 1)
    return max(answer, n - idx[-1] - 1 + idx[0]) + minVal * n



if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)