import math
import sys

def main():
  powers_of_two = set()
  for i in range(1, 36):
    powers_of_two.add(2**i)
  n = int(input())
  a = map(int, raw_input().split())
  numbers_in_array = {}
  for x in a:
    if x in numbers_in_array:
      numbers_in_array[x] += 1
    else:
      numbers_in_array[x] = 1
  out = 0
  for num in numbers_in_array:
    for power in powers_of_two:
      if power - num in numbers_in_array and power - num == num:
        out += numbers_in_array[num] * (numbers_in_array[num] - 1)
      elif power - num in numbers_in_array:
        out += numbers_in_array[num] * numbers_in_array[power - num]

  print out / 2


if __name__ == '__main__':
  main()
