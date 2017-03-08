import sys

n, m = sys.stdin.readline().strip().split(' ')
n = int(n)
m = int(m)
arr = [int(x) for x in sys.stdin.readline().strip().split(' ')]
arr.sort()
brr = [int(x) for x in sys.stdin.readline().strip().split(' ')]
for i in xrange(m):
    left = 0
    right = n
    while left < right:
        mid = (left + right) / 2
        if arr[mid] <= brr[i]:
            left = mid + 1
        else:
            right = mid
    print left,
print
