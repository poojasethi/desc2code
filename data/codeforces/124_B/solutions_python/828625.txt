from itertools import permutations as perm

n, k = [int(x) for x in raw_input().split()]

nums = []
for i in range(n):
    nums.append(raw_input())
l = range(1, k+1)

def arrange(i, p):
    s = ""
    for n in p:
        s += i[n-1]
    return s

def rearrange(nums, p):
    nnums = []
    for i in nums:
        nnums.append(int(arrange(i, p)))
    return nnums
m = float("inf")
for p in perm(l):
    newl = rearrange(nums, p)
    mmax = max(newl)
    mmin = min(newl)
    m = min(m, mmax-mmin)

print m


