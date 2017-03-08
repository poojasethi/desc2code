import math
import heapq

n, k = map(int, raw_input().split())
towers = map(int, raw_input().split())
towers = [[towers[i], i] for i in range(len(towers))]
towers.sort()
min_stability = towers[-1][0] - towers[0][0]
best_moves = 0

if n == 1:
  print min_stability, best_moves
  exit()

moves = []
for i in range(k):
  towers[-1][0] -= 1
  towers[0][0] += 1
  moves.append((towers[-1][1] + 1, towers[0][1] + 1))
  towers.sort()
  stability = towers[-1][0] - towers[0][0]
  if stability < min_stability:
    min_stability = stability
    best_moves = i + 1

print min_stability, best_moves
for i in range(best_moves):
  print moves[i][0], moves[i][1]
