def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def is_A_superset_of_B(a, b):
    d = gcd(a, b)
    while d != 1:
        b /= d
        d = gcd(a, b)
    return a % b == 0


def main():
    tc = int(raw_input())
    for _ in xrange(tc):
        A, B = map(long, raw_input().split())
        print ("Yes" if is_A_superset_of_B(A, B) else "No")


if __name__ == '__main__':
    main()
