s = raw_input().split("heavy")
print sum(s[i].count("metal")*i for i in xrange(len(s)))
