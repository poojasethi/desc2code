s = map(int, raw_input().split(":"))
t = map(int, raw_input().split(":"))
#[a,b] = map(int, raw_input().split())

minute = s[1] - t[1]
hour = s[0] + 24 - t[0]
if minute < 0:
    minute += 60
    hour -= 1

if hour >= 24:
    hour -= 24

print "%02d:%02d" % (hour,minute)
