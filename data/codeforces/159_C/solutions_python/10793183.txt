#!/usr/bin/env python2.6
import sys
from collections import defaultdict

class name:
  def __init__(self, s):
    self.name = s
    self.dict = defaultdict(list)
    for i, c in enumerate(s):
      self.dict[c].append(i)
    self.deleted = set()

  def query(self, occur, char):
    i = self.dict[char].pop(occur-1)
    self.deleted.add(i)

  def write(self):
    for i, c in enumerate(self.name):
      if i not in self.deleted:
        sys.stdout.write(c)
    print

k = int(raw_input())
inname = raw_input() * k
mname = name(inname)
n = int(raw_input())
for i in xrange(n):
  line = raw_input().split(' ')
  mname.query(int(line[0]), line[1])

mname.write()



