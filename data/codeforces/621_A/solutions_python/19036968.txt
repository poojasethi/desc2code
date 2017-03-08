raw_input()
nums = sorted(map(int, raw_input().split()))
odd = filter(lambda a: a % 2 == 1, nums) + [sum(nums)]
print sum(nums) if sum(nums) % 2 == 0 else sum(nums) - odd[0]
