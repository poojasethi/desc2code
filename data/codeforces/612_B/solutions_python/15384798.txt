__author__ = 'trunghieu11'


def solve(n, A):
    files = []
    for i in range(n):
        files.append((A[i], i))
    files = sorted(files)
    answer = 0
    for i in range(1, n):
        answer += abs(files[i][1] - files[i - 1][1])
    return answer


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)