inversion=0
def merge(array,i,j):
	global inversion
	# raw_input()
	# print i,j
	if(j==i):
		return [array[i]]
	else:
		array1 = merge(array,i,(j+i)/2)
		array2 = merge(array,(j+i)/2+1,j)
		# print array1, array2
		retarr = []
		while( len(array2)>0 and len(array1)>0 ):
			if(array1[0]>array2[0]):
				retarr.append(array2.pop(0))
				inversion+=len(array1)
			else:
				retarr.append(array1.pop(0))
		# inversion+=len(array1)
		retarr=retarr +array1+array2
		return retarr
num = []
n = int(raw_input())
num = map(int,raw_input().split())
result = merge(num,0,n-1)
# for i in range(0,100000):
	# print result.pop(0)
print inversion