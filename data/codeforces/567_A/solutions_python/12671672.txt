__author__ = 'trunghieu11'

def main():
    n = int(raw_input())
    A = map(int, raw_input().split())
    for i in range(n):
        print min(A[i + 1] - A[i] if i + 1 < n else 10 ** 10, A[i] - A[i - 1] if i - 1 >= 0 else 10 ** 10), max(A[i] - A[0], A[n - 1] - A[i])

if __name__ == '__main__':
    main()