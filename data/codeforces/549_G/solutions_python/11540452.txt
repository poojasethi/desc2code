import math
import sys

def main():
  n = int(raw_input())
  nums = map(int, raw_input().split())
  for i in range(len(nums)):
    nums[i] = nums[i] - n + i  + 1
  nums.sort()
  nums.append(100000000);
  for i in range(n - 1, -1, -1):
    if nums[i] == nums[i+1]:
      print ':('
      return
  for i in range(n):
    print nums[i] + n - i - 1,


if __name__ == '__main__':
  main()
