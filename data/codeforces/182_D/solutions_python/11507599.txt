""" 
    Author: Hemanth Kumar Veeranki
    Handle:harry7

"""
#!/usr/bin/python
s1=raw_input()
s2=raw_input()
dic={}
ans=0
for i in range(len(s1)):
   s3=s1[:i+1]
   if(s3)*(len(s1)/len(s3))==s1:
      dic.setdefault(s3,0)
      dic[s3]+=1
for i in range(len(s2)):
   s3=s2[:i+1]
   if(s3)*(len(s2)/len(s3))==s2:
      dic.setdefault(s3,0)
      dic[s3]+=1
      if(dic[s3]==2):ans+=1
print ans
