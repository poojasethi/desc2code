def check_simple(s):
    r = s[0]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in range(0, len(s) - 1):
        if r[x] == s[x+1]:
            y = alphabet.index(r[x])
            y = y + 1
            if y > 25:
                y = y - 26
            if x < len(s) - 2:
                if alphabet[y] == s[x+2]:
                    y = y + 1
            if y > 25:
                y = y - 26
            r = r + alphabet[y]
        else:
            r = r + s[x+1]
    return r


s = raw_input()
print check_simple(s)
