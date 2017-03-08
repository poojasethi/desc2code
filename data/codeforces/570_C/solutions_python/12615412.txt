range = xrange; input = raw_input
argmax = lambda l: l.index(max(l))
argmin = lambda l: l.index(min(l))

def read_list(t): return [t(x) for x in input().split()]
def read_line(t): return t(input())
def read_lines(t, N): return [t(input()) for _ in range(N)]

N, M = read_list(int)
S = list(read_line(str))

i = 0
ans = 0
while i < N:
    if S[i] == '.':
        start = i
        while i < N and S[i] == '.':
            i += 1
        ans += i - start - 1
    i += 1

for i in range(M):
    x, c = input().split()
    x = int(x) - 1
    if N == 1:
        print(0)
        continue
    if c == '.' and S[x] != '.':
        ans += (x < N - 1 and S[x+1] == '.') + (x > 0 and S[x-1] == '.')
    elif c != '.' and S[x] == '.':
        ans -= (x < N - 1 and S[x+1] == '.') + (x > 0 and S[x-1] == '.')
    S[x] = c
    print(ans)
