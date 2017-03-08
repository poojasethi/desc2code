import math
import sys

def main():
  n, m = map(int, raw_input().split())
  notes = []
  for i in range(m):
    notes.append(map(int, raw_input().split()))
  notes.sort()
  best = 0
  for i in range(len(notes) - 1):
    day_diff = notes[i + 1][0] - notes[i][0]
    height_diff = notes[i + 1][1] - notes[i][1]
    if abs(height_diff) > day_diff:
      print 'IMPOSSIBLE'
      return
    if height_diff > 0:
      days_left = day_diff - height_diff
      additional = days_left / 2
      if notes[i + 1][1] + additional > best:
        best = notes[i + 1][1] + additional
    else:
      days_left = day_diff - abs(height_diff)
      additional = days_left / 2
      if notes[i][1] + additional > best:
        best = notes[i][1] + additional

  # Beginning
  day_diff = notes[0][0] - 1
  best = max(notes[0][1] + day_diff, best)
  # End
  day_diff = n - notes[-1][0]
  best = max(notes[-1][1] + day_diff, best)
  print best

if __name__ == '__main__':
  main()
