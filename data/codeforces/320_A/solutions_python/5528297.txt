import sys
import re

line = sys.stdin.readline().strip()

match = re.compile("^((1)|(14)|(144))+$").match(line)
if match:
  print "YES"
else:
  print "NO"
