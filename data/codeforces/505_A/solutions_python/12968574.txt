def is_pal(s):
    return s == s[::-1]

def main():
    s = raw_input()
    n = len(s)
    for i in xrange(n + 1):
        for j in xrange(26):
            c = chr(ord('a') + j)
            new_word = s[:i] + c + s[i:]
            if is_pal(new_word):
                print new_word
                return
    print "NA"

if __name__ == '__main__':
    main()
