c1,c2,c3,c4 = [int(x) for x in raw_input().split()]
n , m =[int(x) for x in raw_input().split()]
bus = [int(x) for x in raw_input().split()]
trol = [int(x) for x in raw_input().split()]

busc1= []
bussum = 0
trolsum = 0
for x in bus:
	bussum += min(x*c1 , c2)
for x in trol:
	trolsum += min(x*c1,c2)
	
res = min(bussum,c3) + min(trolsum,c3)
res=min(res,c4)
print(res)	
