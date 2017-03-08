#http://codeforces.com/contest/518/problem/A
#solved by Benegripe
#!/usr/bin/python
s = raw_input()
t = raw_input()
n = len(s)-1
while s[n] == 'z':
    s = s[0:n] + 'a' + s[n+1:]
    n -= 1
s = s[0:n] + chr(ord(s[n])+1) + s[n+1:len(t)]
print "No such string" if s == t else s
