n,k = [int(x) for x in raw_input().split(" ")]
list1=[int(x) for x in raw_input().split(" ")]
list1.sort()
list1.reverse()
print list1[k-1]