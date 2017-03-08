s = raw_input()

count = 1
grabbed = 1

for i in range(1, len(s)):
    if s[i]==s[i-1] and grabbed<5:
        grabbed += 1
    else:
        count += 1
        grabbed = 1
print count

