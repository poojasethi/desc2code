__author__ = 'trunghieu11'


def solve(n, k, A):
    left = {}
    right = {}
    answer = 0
    for x in A:
        if x in right:
            right[x] += 1
        else:
            right[x] = 1
    for x in A:
        right[x] -= 1
        if x % k == 0 and x / k in left and x * k in right:
            answer += left[x / k] * right[x * k]
        if x in left:
            left[x] += 1
        else:
            left[x] = 1
    return answer


if __name__ == '__main__':
    n, k = map(int, raw_input().split(" "))
    A = map(int, raw_input().split(" "))
    print solve(n, k, A)