n = int(raw_input().strip())
words = []
for _ in xrange(n):
    words.append(raw_input().strip())
words = "<3" + "<3".join(words) + "<3"
garbage = raw_input().strip()
wi = 0
gi = 0
wl = len(words)
gl = len(garbage)
allowed = map(chr, xrange(97, 123)) + map(chr, xrange(48, 58)) + ["<", ">"]

while wi < wl and gi < gl:
    if words[wi] == garbage[gi]:
        gi += 1
        wi += 1
    elif garbage[gi] in allowed:
        gi += 1
    else:
        print "no"
        exit()

if wi == wl:
    print "yes"
else:
    print "no"
