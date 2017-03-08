import math

def sieve(max_size=1000000000):
    maxi = int(math.sqrt(max_size)) + 2
    res = []
    primes = [True] * maxi
    primes[0] = False
    primes[1] = False
    for i in range(2, maxi):
        if primes[i]:
            res.append(i)
            for j in range(i * 2, maxi, i):
                primes[j] = False
    return res

def is_prime(n, primes):
    stop = math.sqrt(n) + 1
    for p in primes:
        if p > stop: return True
        if n % p == 0 and n != p: return False
    return True

def solve(n, m, primes):
    return '\n'.join((str(x) for x in range(max(2, n), m + 1) if is_prime(x, primes)))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        N, M = map(int, raw_input().split())
        if _ > 0: print ''
        res = solve(N, M, sieve())
        print '{}'.format(res)
