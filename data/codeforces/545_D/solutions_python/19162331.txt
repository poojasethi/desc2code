n, nums, s, t = int(raw_input()), sorted(map(int, raw_input().split())), 0, 0
for i in xrange(0, n):
    if s <= nums[i]:
        t += 1
        s += nums[i]
print t
