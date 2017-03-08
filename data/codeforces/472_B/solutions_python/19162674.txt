n, k = map(int, raw_input().split())
nums = sorted(map(int, raw_input().split()), reverse=True)
t = 0
for i in xrange(0, n, k):
    t += 2 * max(nums[i:min(n, i+k)]) - 2
print t
