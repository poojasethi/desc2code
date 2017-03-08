


s = raw_input()


for i in xrange(len(s)+1):
  for j in xrange(26):
    l = [ _ for _ in s ]
    l.insert(i, chr( ord('a') + j))
    if ''.join( l[:len(l)/2] ) == ''.join( l[::-1][:len(l)/2] ):
      print ''.join(l)
      exit(0)

print 'NA'
