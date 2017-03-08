input = raw_input().split('/')
cat = ''
for i in input:
    if i != '':
        cat += '/'+i
if cat == '':
    print '/'
else:
    print cat
