n = input ()
m = [map (int, raw_input ().split ()) for _ in xrange (n)]
record = [i for i in xrange (1, n + 1)]
for ind, ele in enumerate (m, 1):
    for x in ele:
        if x == 1 or x == 3:
            record.remove (ind);break
         
print len (record)
for x in record: print x,