# -*- coding: utf-8 -*-

s = raw_input()
t = raw_input()
import string
lower = string.lowercase
upper = lower.upper()

class mydict(dict):

  def __missing__(self, key):
    self[key] = 0
    return self[key]

ds = mydict()
dt = mydict()

for i in s:
  ds[i] += 1

for i in t:
  dt[i] += 1

cnt1 = 0
cnt2 = 0

for key in ds:
  t = min( ds[key], dt[key] )
  ds[key] -= t
  dt[key] -= t
  cnt1 += t

for key in lower:
  if ds[key] and dt[key.upper()]:
    cnt2 += min( ds[key] , dt[key.upper()] )

for key in upper:
  if ds[key] and dt[key.lower()]:
    cnt2 += min( ds[key] , dt[key.lower()] )

print cnt1, cnt2
