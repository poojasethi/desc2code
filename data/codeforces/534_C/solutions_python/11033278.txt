import math
import sys

def main():
  n, s = map(int, raw_input().split())
  nums = map(int, raw_input().split())
  minimum = len(nums)
  maximum = sum(nums)
  nums = [(nums[i], i) for i in range(len(nums))]
  nums.sort(reverse = True)
  index_map = {}
  length = n
  for num in nums:
    if num[0] == 1:
      maximum -= 1
      minimum -= 1
      s -= 1
      index_map[num[1]] = 0
      length -= 1
  if length == 1:
    for num in nums:
      if num[0] != 1:
        index_map[num[1]] = num[0] - 1
  else:
    for num in nums:
      minus_1 = num[0] - 1
      if minus_1 == 0:
        continue
      if (s - minimum) < minus_1:
        index_map[num[1]] = minus_1 - (s - minimum)
        if (maximum - s) < minus_1:
          index_map[num[1]] += minus_1 - (maximum - s)
      elif (maximum - s) < minus_1:
        index_map[num[1]] = minus_1 - (maximum - s)
      else:
        index_map[num[1]] = 0
  for i in range(n):
    print index_map[i],


if __name__ == '__main__':
  main()
