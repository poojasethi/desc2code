n = input()
b = sorted(map(int, raw_input().split()))
bb = [0] * 5100
cardA = list()
cardB = list()
for i, v in enumerate(b):
  if bb[v] == 0:
    cardA.append(v)
    bb[v] += 1
  elif bb[v] == 1:
    cardB.append(v)
    bb[v] += 1

cardB = cardB[::-1]
if len(cardB) > 0:
  if cardA[len(cardA) - 1] == cardB[0]:
    cardB = cardB[1:]
print len(cardA) + len(cardB)
for i in cardA:
  print i,
for i in cardB:
  print i,
print
