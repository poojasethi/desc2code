n = input()
card = map(int, raw_input().split())
score = [0, 0]
t = 0
while len(card) > 0:
  r = card[len(card) - 1]
  l = card[0]
  if r > l:
    score[t] += r
    card = card[:len(card) - 1]
  else:
    score[t] += l
    card = card[1:]
  t = (t + 1) % 2
print "%d %d" % (score[0], score[1])
