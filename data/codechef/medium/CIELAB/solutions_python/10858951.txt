test = map(int,raw_input().split())
count = str(abs(test[0] - test[1]))
l = ['1','2','3','4','5','6','7','8','9']
l.remove(count[0])
string = ''
string += l[0]
string += count[1:len(count)+1]
print int(string)