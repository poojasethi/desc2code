n = int(raw_input())
num = str(raw_input())

# n = 7
# num = "1198733"
num_str = ""

if (n % 2) is 0:
  i = 0
else:
  num_str += str(num[0:3])
  i = 3
  if i is not n:
    num_str += "-"

while i < n:
  #print i
  num_str += str(num[i:i+2])
  if i + 2 is not n:
    num_str += "-"
  i += 2

print num_str