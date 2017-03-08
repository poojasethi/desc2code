import re
n=raw_input()
n=int(n)
for i in range(0,n):
    line=raw_input()
    m=re.match(r'R(\d+)C(\d+)',line)
    if m:
        y=int(m.group(2))
        s=''
        while y!=0:
            c=(y-1)%26+ord('A')
            s=chr(c)+s
            y=(y-1)/26
        print(s+m.group(1))
    else:
        t=re.match(r'(\D+)(\d+)',line)
        x=0
        for i in t.group(1):
            x=x*26+ord(i)-ord('A')+1
        print('R%dC%d' %(int(t.group(2)),x))
            
      
