__author__ = 'trunghieu11'

def calc(n, A, val):
    answer = 0
    counter = 0
    sameCounter = 0
    cur = A[0]
    same = A[0]
    i = 0
    while i < len(A):
        if A[i] == cur or A[i] + val == cur:
            counter += 1
        else:
            answer = max(answer, counter)
            if i - 1 >= 0 and A[i - 1] + val == A[i]:
                counter = sameCounter + 1
                cur = A[i]
            else:
                counter = 1
                cur = A[i]

        if same == A[i]:
            sameCounter += 1
        else:
            same = A[i]
            sameCounter = 1
        i += 1

    return max(answer, counter)

def solve(n, A):
    return max(calc(n, A, 1), calc(n, A, -1))

if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split(" "))
    print solve(n, A)