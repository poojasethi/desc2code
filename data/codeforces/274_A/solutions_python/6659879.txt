n, k = map(int, raw_input().split())
nums = list(map(int, raw_input().split()))
nums.sort(reverse=True)
chosen = set()
for num in nums:
    if num * k not in chosen:
        chosen.add(num)
print len(chosen)