
words = raw_input()
words = words.replace (',', ';')
words = words.split (';')

a = ""
b = ""

for word in words:
    if word == '':
        b += ','
        continue
    try:
        x = int(word)
        if (word[0] == "0" and len(word) != 1):
            raise Exception('aaa')
        a += word + ","
    except:
        b += word + ','

if a == "":
    print "-"
else:
    print '"' + a[:-1] + '"'
    
if b == "":
    print "-"
else:
    print '"' + b[:-1] + '"'
