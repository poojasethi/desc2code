a=list(map(int,raw_input().split()))
b=list(map(int,raw_input().split()))
arr=[]
for i in range(1,len(a)):
    for j in range(1,len(b)):
        arr.append(abs(a[i]-b[j]))
arr=sorted(arr)
print arr[0]