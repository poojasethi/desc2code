
if __name__ == '__main__':
    n = map(int, raw_input().split(' '))[0];
    m = map(int, raw_input().split(' '));

    for i, elem in enumerate(m):
        m[i] = (elem, i)

    m = sorted(m, key=lambda x: x[0])
    ans = 0
    for i in range(1, n):
        ans += abs(m[i][1] - m[i-1][1])

    print ans
