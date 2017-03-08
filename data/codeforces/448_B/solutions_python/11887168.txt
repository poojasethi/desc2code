def isss(s,s1):
    ln= len(s1)
    lll= len(s)
    i=0
    j=0
    while i<ln and j<lll:
        if s1[i]==s[j]:
            j=j+1
        i=i+1
    if j==lll:
        return True
    return False
def main():
    s = raw_input()
    s2= raw_input()
    if ''.join(sorted(s)) == ''.join(sorted(s2)):
        print("array")
        return 0;
    if isss(s2,s) == True:
        print("automaton")
        return 0;
    if isss(sorted(s2),sorted(s)):
        print("both")
        return 0;
    print("need tree")
#print(isss('tomat','automaton'))
main()
