a = raw_input()
print [a.lower(), a.upper()][sum( map(str.isupper, a) )*2 > len(a)]