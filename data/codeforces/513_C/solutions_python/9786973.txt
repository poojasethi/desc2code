
n = int(raw_input())

s = []

x = []

for i in xrange(n):
  l, r = map( int, raw_input().split() )
  s.append( [l, r] )
  x.append(l)
  x.append(r)

x.sort()


res = 0.

for ans in xrange (1, 10001):

  for t in xrange(1<<n):
    cnt = 0
    for i in xrange(n):
      if (t>>i)&1:
        cnt += 1
    if cnt < 2: continue

    prob = 1.
    for i in xrange(n):
      a = s[i][0]
      b = s[i][1]
      if (t>>i)&1:
        if a < ans: a = ans
      else:
        if b > ans-1: b = ans-1
      if a > b:
        prob = 0.
        break

      prob *= 1.*(b-a+1) / (s[i][1] - s[i][0]+1)

    res += prob 

# end




interval = []
def dfs(idx, prob):
  if idx == n:
    global ans
    tmp = [i for i in interval]
    tmp.sort(reverse=True)

    if tmp[0] != tmp[1]:
      ans += prob*sum(tmp[1])/2
    else:
      i = 1
      while i+1 < n and tmp[i+1] == tmp[i]: i+=1
      l, r = tmp[0]
      if l == r:
        ans += prob*l
        return
      c = 0.
      i += 1
      m = i
      for i in xrange(l, r+1):
        #c += 1.*j*(r-j+1)/(r-l+1)  * (j/(r-l+1)) ** (i-2)  / (r-l+1)  * (i)*(i-1)
        c += 1.*i*(r-i+1)/(r-l+1) * (1.*i/(r-l+1))**(m-2)/(r-l+1)*m*(m-1)
      ans += prob*c
    return
  l, r = s[idx]
  p = set()
  p.add(l)
  p.add(r)
  for i in x:
    if i >= l and i <= r:
      p.add(i)
  p = list(p)
  p.sort()
  for i in xrange(1, len(p)):
    sel = [ p[i-1], p[i]-1 ]
    interval.append(sel)
    dfs( idx+1, prob*(p[i]-p[i-1])/(r-l+1) )
    interval.pop()

  sel = [ p[-1], p[-1] ]
  interval.append(sel)
  dfs(idx+1,  prob/(r-l+1))
  interval.pop()

#dfs(0, 1.)

print res
