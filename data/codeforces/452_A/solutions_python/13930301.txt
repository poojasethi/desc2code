import re
n = int(raw_input())
l = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
s = raw_input()
for e in l:
    if re.match( s+'$', e) :
        print e.lower()