#! /usr/bin/env python

def main():
	d={}
	n=input()
	t=n
	while t: 
		b=raw_input()
		if d.has_key(b):
			d[b]+=1
		else:
			d[b]=1
				
		t-=1
	inverse = [(key, value) for key, value in d.items()]
	inverse=sorted(inverse)
	for key,value in inverse:
		print key,value	
	
	
if __name__=="__main__":
    main()
