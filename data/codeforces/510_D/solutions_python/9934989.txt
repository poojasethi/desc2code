from collections import defaultdict
from fractions import gcd
def inf(): return 10**9+7
    
N = int(raw_input())
L = map(int,raw_input().split())
C = map(int,raw_input().split())

S = defaultdict(inf)
S[0] = 0
for i in xrange(N):
    T = defaultdict(inf)
    for l in S:
        r = gcd(l,L[i])
        T[r] = min(T[r], S[l]+C[i])
    for r in T:
        S[r] = min(S[r], T[r])
print S[1] if 1 in S else -1
