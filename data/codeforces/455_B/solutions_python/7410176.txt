class tree(object):
    def __init__(self, c=''):
	self.c = c 
	self.sons = {}
    
    def insert(self,s):
	if s == '':
	    return
	self.sons.setdefault(s[0], tree(s[0]))
        self.sons[s[0]].insert(s[1:])

    def cal(self, v):
	if self.sons == {}:
	    return v
	flag = 1
	for i in self.sons:
	    if self.sons[i].cal(v) == 1: 
		flag = 0
        return flag

n, k = map(int, raw_input().split())
r = tree()
for i in range(n):
    r.insert(raw_input())

f,g = 0,0
for i in r.sons:
    if r.sons[i].cal(1) == 1:
	f = 1
    if r.sons[i].cal(0) == 1:
	g = 1

if f == 1 and g == 1:
    print 'First'
elif f == 0 and g == 0:
    print 'Second'
elif f == 0 and g == 1:
    print 'Second'
elif k % 2 == 0:
    print 'Second'
else :
    print 'First'
