def isSorted(arr):
    for n in range(len(arr)-1):
        if arr[n] > arr[n+1]:
            return False
    return True

n = int(raw_input())
arr = map(int,raw_input().split())

while not isSorted(arr):
    for n in range(len(arr)-1):
        if arr[n] > arr[n+1]:
            arr[n],arr[n+1] = arr[n+1], arr[n]
            print n+1,n+2
