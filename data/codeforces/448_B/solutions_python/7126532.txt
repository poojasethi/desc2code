import sys
s = raw_input()
t = raw_input()

def subsequence(a, b):
    #check if b is a subsequence of a
    bpos = 0
    blen = len(b)
    for i, c in enumerate(a):
        if bpos < blen and c == b[bpos]:
            bpos += 1
    return bpos == blen

# automaton if t is subsequence of s
automaton = subsequence(s, t)
if automaton:
    print "automaton"
    sys.exit(0)

# array if t is permutation of s
array = sorted(s) == sorted(t)
if array:
    print "array"
    sys.exit(0)

both = subsequence(sorted(s), sorted(t))

if both:
    print "both"
else:
    print "need tree"
